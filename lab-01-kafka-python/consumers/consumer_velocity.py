from kafka import KafkaConsumer
from collections import defaultdict, deque
from datetime import datetime, timedelta
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    group_id='velocity-detector-v1',
    auto_offset_reset='earliest'
)

# Dla każdego user_id trzymamy kolejkę timestampów z ostatnich 60 sekund
user_events = defaultdict(deque)

WINDOW_SECONDS = 60
THRESHOLD = 3

print("Nasłuchuję anomalii prędkości: > 3 transakcje / 60 s dla tego samego user_id...")

for message in consumer:
    event = message.value

    user_id = event.get("user_id")
    tx_id = event.get("tx_id")
    amount = event.get("amount")
    store = event.get("store")
    category = event.get("category")
    ts_raw = event.get("timestamp")

    if not user_id or not ts_raw:
        print(f"Pominięto niepoprawne zdarzenie: {event}")
        continue

    try:
        # Producent wg laba wysyła aktualny czas ISO
        event_time = datetime.fromisoformat(ts_raw)
    except ValueError:
        print(f"Niepoprawny timestamp w zdarzeniu: {event}")
        continue

    queue = user_events[user_id]
    queue.append(event_time)

    # Usuwamy wszystko starsze niż 60 sekund względem bieżącego zdarzenia
    window_start = event_time - timedelta(seconds=WINDOW_SECONDS)
    while queue and queue[0] < window_start:
        queue.popleft()

    tx_count_in_window = len(queue)

    if tx_count_in_window > THRESHOLD:
        print(
            f"ALERT: user={user_id} wykonał {tx_count_in_window} transakcji "
            f"w ciągu ostatnich {WINDOW_SECONDS} s | "
            f"tx_id={tx_id} | amount={amount} PLN | {store} | {category} | ts={ts_raw}"
        )
    else:
        print(
            f"OK: user={user_id} | liczba transakcji w oknie 60 s = {tx_count_in_window}"
        )
