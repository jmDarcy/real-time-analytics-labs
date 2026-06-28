# Real-Time Analytics Labs

This repository contains practical lab materials for a Real-Time Analytics course. The structure follows the topics used in the RTA2026 teaching materials:

<https://sebkaz-teaching.github.io/RTA2026/>

The labs focus on event-driven data processing, Kafka producers and consumers, Apache Spark, Spark Structured Streaming, Kafka integration, REST APIs, and simple real-time model serving examples.

## Repository Structure

```text
real-time-analytics-labs/
|-- lab-01-kafka-python/
|   |-- producers/
|   `-- consumers/
|-- lab-02-apache-spark/
|-- lab-03-structured-streaming/
|-- lab-04-spark-streaming-kafka/
|-- lab-05-flask-rest-api/
|-- lab-06-fastapi-fraud-detection/
|-- lab-07-structured-data-modeling/
|-- lab-08-unstructured-data-tensors/
|-- homework/
|   |-- homework-01-kafka-velocity-consumer/
|   `-- homework-02-spark-transactions/
|-- .gitignore
`-- README.md
```

## Lab Overview

| Folder | Topic | Description |
| --- | --- | --- |
| `lab-01-kafka-python` | Kafka in Python | Basic Kafka producers and consumers, including filtering, enrichment, counting, statistics, and velocity-oriented consumers. |
| `lab-02-apache-spark` | Apache Spark | Batch-oriented Spark exercises using transaction data and notebook-based exploration. |
| `lab-03-structured-streaming` | Spark Structured Streaming | File-based streaming examples, stream generation, rate control, and basic streaming transformations. |
| `lab-04-spark-streaming-kafka` | Spark Structured Streaming with Kafka | Kafka-backed streaming examples with raw and text topics, producers, and Spark integration. |
| `lab-05-flask-rest-api` | Flask and REST APIs | Introductory API examples with Flask, HTTP routes, request handling, and service testing from notebooks. |
| `lab-06-fastapi-fraud-detection` | FastAPI and model serving | Simple fraud-detection model training and API serving with FastAPI. |
| `lab-07-structured-data-modeling` | Structured data: NumPy, Pandas, PyTorch, SQLite | Notes and a compact example for working with tabular data, tensors, simple classification, and storing predictions in SQLite. |
| `lab-08-unstructured-data-tensors` | Unstructured data: tensors, images, text, pretrained models | Notes and lightweight examples for representing images and text as tensors before using pretrained model pipelines. |
| `homework` | Homework assignments | Course homework materials aligned with the lab sequence. |

## Prerequisites

The exact runtime depends on the lab. In general, the materials assume a Python/Jupyter environment with selected components from the RTA2026 course stack:

- Python 3.10 or newer,
- Jupyter Notebook or JupyterLab,
- Apache Kafka for Kafka-based labs,
- Apache Spark / PySpark for Spark labs,
- Flask or FastAPI for API labs,
- common Python data and ML packages such as `pandas`, `scikit-learn`, and `requests`.

For Kafka and Spark labs, follow the runtime setup described in the RTA2026 course materials. Some examples expect Kafka brokers, Spark sessions, or notebook kernels to be already available.

## Suggested Study Path

1. Start with `lab-01-kafka-python` to understand producers, consumers, topics, and event flow.
2. Move to `lab-02-apache-spark` for Spark basics on transaction-style data.
3. Continue with `lab-03-structured-streaming` to move from batch processing to streaming.
4. Use `lab-04-spark-streaming-kafka` to combine Spark Structured Streaming with Kafka topics.
5. Review `lab-05-flask-rest-api` to understand how analytical results can be exposed through HTTP APIs.
6. Finish with `lab-06-fastapi-fraud-detection` for a compact example of real-time model serving.
7. Use `lab-07-structured-data-modeling` to connect structured tabular data with tensors, simple models, and SQLite persistence.
8. Use `lab-08-unstructured-data-tensors` to review how unstructured data such as images and text are represented before model inference.

## Running the Materials

Most labs are notebook-first. Open the relevant notebook in JupyterLab and run the cells in order.

For script-based Kafka examples, start the required Kafka services first, then run producers and consumers from separate terminals. For API examples, run the Flask or FastAPI application and test it with `requests`, browser calls, or the notebook cells provided in the lab.

## Notes

- The repository is educational and mirrors course exercises rather than a production deployment.
- Data files and models included in the labs are examples for local experimentation.
- API and fraud-detection examples are intentionally small so that the real-time analytics architecture is easy to inspect.
- The RTA2026 course page should be treated as the reference source for the conceptual sequence and runtime assumptions.
