# Lab 07: Structured Data, Tensors, Models, and SQLite

This lab extends the course sequence after Kafka, Spark, streaming, REST APIs, and model serving. It follows the RTA2026 Lab 7 theme: structured data, NumPy, Pandas, PyTorch tensors, simple models, and relational storage with SQLite.

Reference course material:

<https://sebkaz-teaching.github.io/RTA2026/>

## Learning Goals

- Review the difference between structured, semi-structured, and unstructured data.
- Represent tabular data as arrays, DataFrames, and tensors.
- Train or sketch a compact classifier for structured observations.
- Store scored observations and model outputs in SQLite.
- Keep the example small enough to inspect during a lab session.

## Files

| File | Purpose |
| --- | --- |
| `structured_data_notes.md` | Conceptual notes aligned with the Lab 7 topic. |
| `structured_data_sqlite_demo.py` | End-to-end example using generated tabular data, a simple classifier, and SQLite persistence. |

## Suggested Run

From this folder:

```bash
python structured_data_sqlite_demo.py
```

The script creates a local SQLite database:

```text
structured_predictions.db
```

It stores synthetic customer records, predicted risk labels, and prediction probabilities.

## Discussion Prompt

In a real-time analytics workflow, structured records often arrive continuously but are stored in relational form for audit, replay, and downstream reporting. The important design question is not only how to score a record, but also how to persist the scored event so that the decision can be reproduced later.
