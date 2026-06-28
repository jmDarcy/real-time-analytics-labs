#%%file consumer_enrich.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    group_id='enrich-group',  # ważne: inny niż poprzedni consumer
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Nasłuchuję i wzbogacam transakcje o risk_level...")

for message in consumer:
    transaction = message.value

    amount = transaction["amount"]

    # logika risk_level
    if amount > 3000:
        risk_level = "HIGH"
    elif amount > 1000:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # wzbogacenie eventu
    transaction["risk_level"] = risk_level

    # wypisanie
    print(transaction)
