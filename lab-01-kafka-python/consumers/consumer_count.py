from kafka import KafkaConsumer
from collections import Counter
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    group_id='count-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

store_counts = Counter()
total_amount = {}
msg_count = 0

print("Start agregacji transakcji...")

for message in consumer:
    transaction = message.value

    store = transaction["store"]
    amount = transaction["amount"]

    # 1. licznik transakcji
    store_counts[store] += 1

    # 2. suma kwot
    if store not in total_amount:
        total_amount[store] = 0.0
    total_amount[store] += amount

    # 3. liczba wiadomości globalnie
    msg_count += 1

    # co 10 wiadomości → raport
    if msg_count % 10 == 0:
        print("\n--- PODSUMOWANIE ---")
        print(f"{'Sklep':<10} | {'Liczba':<6} | {'Suma':<10} | {'Średnia':<10}")
        print("-" * 50)

        for store in store_counts:
            count = store_counts[store]
            total = total_amount[store]
            avg = total / count if count > 0 else 0

            print(f"{store:<10} | {count:<6} | {total:<10.2f} | {avg:<10.2f}")

        print("-" * 50)
