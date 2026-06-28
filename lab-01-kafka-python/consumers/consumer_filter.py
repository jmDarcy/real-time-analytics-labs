from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    group_id='filter-group-v2',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Nasłuchuję...")

for message in consumer:
    transaction = message.value
    amount = transaction["amount"]

    if amount > 1000:
        print(f"ALERT: {transaction['tx_id']} | {amount} PLN")

    print(transaction)
