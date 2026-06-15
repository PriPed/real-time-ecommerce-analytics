# Real-Time E-Commerce Analytics Platform

## Overview

A backend data engineering project that processes and analyzes e-commerce events in real time.

The platform simulates an online shopping application where millions of user interactions generate events that are streamed, processed, stored, and exposed through analytics APIs.

Typical events include:

* Product Viewed
* Product Searched
* Product Added to Cart
* Order Placed

The system provides:

* Real-time event ingestion
* Event streaming with Kafka
* Analytics data storage
* Cached API responses
* Daily ETL pipelines
* Data backup to S3
* Reporting tables for business intelligence

---

## Business Problem

Modern e-commerce platforms generate massive amounts of event data every second.

Business teams need answers to questions like:

* Which products are trending?
* What are users searching for?
* How many users abandon their carts?
* What are the peak shopping hours?
* Which categories generate the most revenue?

This project demonstrates how a modern data engineering pipeline can solve these problems.

---

## System Architecture

```
Client / Event Generator
            |
            v
   FastAPI Event Service
            |
            v
          Kafka
            |
            v
     Consumer Service
            |
            v
       PostgreSQL
            |
            v
        Redis Cache
            |
            v
      Analytics APIs
            |
            v
        Dashboard

---------------------------------

          Airflow
              |
              v
        Daily ETL Jobs
              |
              v
          S3 Backup
              |
              v
      Reporting Tables
```

---

## Technology Stack

### Backend

* Python
* FastAPI

### Streaming

* Apache Kafka

### Database

* PostgreSQL

### Cache

* Redis

### Data Pipeline

* Apache Airflow

### Cloud Storage

* AWS S3

### Containerization

* Docker
* Docker Compose

### Tools

* SQLAlchemy
* Pandas
* Git
* GitHub

---

## Features

### Event Ingestion

* Receive user events through REST APIs
* Validate incoming payloads
* Publish events to Kafka topics

### Stream Processing

* Consume Kafka messages
* Transform and enrich events
* Store processed data in PostgreSQL

### Analytics APIs

* Most viewed products
* Most searched products
* Top selling products
* User activity summary
* Revenue metrics

### Redis Caching

* Cache frequently requested analytics
* Reduce database load
* Improve API response times

### ETL Pipeline

* Scheduled using Airflow
* Aggregate daily analytics
* Generate reporting tables
* Backup processed data to S3

---

## Sample Event Payload

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

```
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
│   └── dags/
│
├── analytics/
│
├── database/
│
├── redis/
│
├── docker/
│
├── tests/
│
├── requirements.txt
├── docker-compose.yml
├── README.md
└── .env
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/your-username/real-time-ecommerce-analytics.git

cd real-time-ecommerce-analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

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

### Run Services

```bash
docker-compose up -d
```

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

### Event API

```
POST /events
```

### Analytics APIs

```
GET /analytics/popular-products

GET /analytics/top-searches

GET /analytics/revenue

GET /analytics/user-activity
```

---

## Future Enhancements

* Apache Spark Streaming
* ClickHouse for analytics
* Grafana dashboards
* Elasticsearch integration
* Kubernetes deployment
* CI/CD pipeline with GitHub Actions
* Real-time fraud detection
* Machine learning recommendations

---

## Learning Objectives

This project demonstrates practical experience with:

* Event-Driven Architecture
* Real-Time Data Pipelines
* Apache Kafka
* FastAPI Development
* PostgreSQL Design
* Redis Caching
* Airflow ETL Workflows
* AWS S3 Storage
* Docker Containerization
* Backend System Design

---

## License

This project is intended for educational and portfolio purposes.

