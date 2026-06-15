# Real-Time E-Commerce Analytics Platform

A backend data engineering project that simulates a real-world e-commerce analytics system capable of processing millions of user events in real time. The platform ingests events, streams them through Kafka, stores them in PostgreSQL, caches analytics in Redis, and provides APIs for business insights. Scheduled ETL pipelines using Airflow generate reporting tables and archive data to AWS S3.

---

## Problem Statement

Modern e-commerce platforms generate massive amounts of user activity every second, such as:

* Product Viewed
* Product Searched
* Product Added to Cart
* Order Placed

Businesses need to analyze this data to answer questions like:

* Which products are trending?
* What are the most searched products?
* Which users are most active?
* What is the cart abandonment rate?
* How much revenue is generated daily?
* What are the peak shopping hours?

This project demonstrates how a modern data engineering pipeline can provide both real-time and batch analytics.

---

## System Architecture

```text
                    +----------------------+
                    | Client/Event Generator|
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |  FastAPI Event API   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |        Kafka         |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Consumer Service   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |     PostgreSQL       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      Redis Cache     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    Analytics APIs    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      Dashboard       |
                    +----------------------+

------------------------------------------------------

                    +----------------------+
                    |       Airflow        |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    Daily ETL Jobs    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      AWS S3 Backup   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Reporting Tables   |
                    +----------------------+
```

---

## Technology Stack

### Backend

* Python
* FastAPI

### Event Streaming

* Apache Kafka

### Database

* PostgreSQL

### Caching

* Redis

### Workflow Orchestration

* Apache Airflow

### Cloud Storage

* AWS S3

### Containerization

* Docker
* Docker Compose

### Development Tools

* SQLAlchemy
* Pandas
* Git
* GitHub

---

## Core Features

### Real-Time Event Ingestion

* Accept user events through REST APIs
* Validate event payloads
* Publish events to Kafka topics

### Event Processing

* Consume Kafka messages
* Process and transform events
* Store processed data in PostgreSQL

### Analytics APIs

* Popular products
* Top searched products
* Top selling products
* User activity summary
* Revenue analytics

### Redis Caching

* Cache frequently requested analytics
* Reduce database load
* Improve API response time

### Batch Processing

* Daily ETL jobs using Airflow
* Generate aggregated reporting tables
* Archive processed data to AWS S3

---

## Sample Event

```json
{
    "user_id": 101,
    "product_id": 5001,
    "event_type": "product_viewed",
    "timestamp": "2026-06-15T10:30:00Z"
}
```

---

## Project Structure

```text
real-time-ecommerce-analytics/
│
├── app/
│   ├── api/
│   ├── producers/
│   ├── consumers/
│   ├── models/
│   ├── services/
│   └── config/
│
├── airflow/
│   ├── dags/
│
├── analytics/
├── database/
├── redis/
├── tests/
├── requirements.txt
├── docker-compose.yml
├── .env
├── README.md
└── .gitignore
```

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/real-time-ecommerce-analytics.git

cd real-time-ecommerce-analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Infrastructure

```bash
docker-compose up -d
```

### Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

### Publish Event

```http
POST /events
```

### Get Popular Products

```http
GET /analytics/popular-products
```

### Get Top Searches

```http
GET /analytics/top-searches
```

### Get Revenue Analytics

```http
GET /analytics/revenue
```

### Get User Activity

```http
GET /analytics/user-activity
```

---

## Future Improvements

* Apache Spark Streaming
* ClickHouse for OLAP analytics
* Grafana dashboards
* Elasticsearch integration
* Kubernetes deployment
* GitHub Actions CI/CD
* Machine Learning recommendations
* Real-time fraud detection

---

## Learning Goals

This project demonstrates practical knowledge of:

* Event-Driven Architecture
* Real-Time Data Processing
* Apache Kafka
* FastAPI
* PostgreSQL
* Redis
* Apache Airflow
* AWS S3
* Docker
* Backend System Design
* Data Engineering Best Practices

---

## License

This project is created for learning, portfolio building, and backend data engineering practice.
