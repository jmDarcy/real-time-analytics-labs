# Structured Data Notes

## Data Types

Structured data has a stable schema: rows, columns, types, and constraints. Examples include transactions, customers, payments, telemetry aggregates, and fraud-scoring features.

Semi-structured data has partial structure but flexible fields. JSON events from Kafka are a common example.

Unstructured data does not start as rows and columns. Images, audio, video, and raw text must first be converted into numerical representations.

## Typical Lab 7 Pipeline

```text
raw structured records
-> DataFrame validation
-> numerical feature matrix
-> tensor or array representation
-> simple model
-> scored records
-> SQLite table for persistence and review
```

## Why SQLite Is Useful Here

SQLite is not a streaming engine, but it is practical for lab work because it gives students a real relational database without additional infrastructure. It can be used to persist:

- original observations,
- model inputs,
- predictions,
- prediction timestamps,
- audit fields.

## Real-Time Analytics Connection

Even when scoring is performed online, model outputs need persistence. A scored event should be traceable:

```text
who or what was scored
when the score was produced
which features were used
what decision was recommended
```

This creates the bridge between live analytics and accountable business operations.
