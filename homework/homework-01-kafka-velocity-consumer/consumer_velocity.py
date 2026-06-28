
from kafka import KafkaConsumer
from collections import defaultdict, deque
from datetime import datetime, timedelta
import json

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="broker:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    group_id="velocity-anomaly-consumer"
)

# Dla każdego user_id trzymamy kolejkę timestampów jego transakcji
user_windows = defaultdict(deque)

WINDOW_SECONDS = 60
MAX_TX_ALLOWED = 3

print("Nasłuchuję anomalii prędkości: > 3 transakcje / 60 sekund...")

for message in consumer:
    event = message.value

    user_id = event.get("user_id")
    tx_id = event.get("tx_id")
    amount = event.get("amount")
    timestamp_str = event.get("timestamp")

    if user_id is None or timestamp_str is None:
        print(f"Pominięto błędny event: {event}")
        continue

    # Producent z Lab 1 generuje timestamp w formacie ISO
    event_time = datetime.fromisoformat(timestamp_str)

    window_start = event_time - timedelta(seconds=WINDOW_SECONDS)

    # Usuwamy transakcje starsze niż 60 sekund
    user_queue = user_windows[user_id]

    while user_queue and user_queue[0] < window_start:
        user_queue.popleft()

    # Dodajemy aktualną transakcję
    user_queue.append(event_time)

    # Jeśli w ostatnich 60 sekundach jest więcej niż 3 transakcje → ALERT
    if len(user_queue) > MAX_TX_ALLOWED:
        print(
            f"ALERT VELOCITY: user_id={user_id} | "
            f"liczba_transakcji={len(user_queue)} w 60s | "
            f"ostatnia_tx={tx_id} | amount={amount} | timestamp={timestamp_str}"
        )
    else:
        print(
            f"OK: user_id={user_id} | "
            f"liczba_transakcji_w_60s={len(user_queue)} | tx={tx_id}"
        )
