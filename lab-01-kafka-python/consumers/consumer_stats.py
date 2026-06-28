from kafka import KafkaConsumer
from collections import defaultdict
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    group_id='stats-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# struktura:
# stats[category] = {
#     'count': int,
#     'total': float,
#     'min': float,
#     'max': float
# }
stats = defaultdict(lambda: {
    'count': 0,
    'total': 0.0,
    'min': float('inf'),
    'max': float('-inf')
})

msg_count = 0

print("Start zbierania statystyk per kategoria...")

for message in consumer:
    transaction = message.value

    category = transaction["category"]
    amount = transaction["amount"]

    # aktualizacja statystyk
    stats[category]['count'] += 1
    stats[category]['total'] += amount
    stats[category]['min'] = min(stats[category]['min'], amount)
    stats[category]['max'] = max(stats[category]['max'], amount)

    msg_count += 1

    # raport co 10 wiadomości
    if msg_count % 10 == 0:
        print("\n--- STATYSTYKI PER KATEGORIA ---")
        print(f"{'Kategoria':<15} | {'Liczba':<6} | {'Suma':<10} | {'Min':<8} | {'Max':<8}")
        print("-" * 70)

        for cat, data in stats.items():
            print(
                f"{cat:<15} | "
                f"{data['count']:<6} | "
                f"{data['total']:<10.2f} | "
                f"{data['min']:<8.2f} | "
                f"{data['max']:<8.2f}"
            )

        print("-" * 70)
