# 🚀 Real-Time News Sentiment Analytics Dashboard

A fully automated cloud-native news analytics pipeline built using AWS services, PostgreSQL, Docker, and Streamlit.

This project collects live news articles from NewsAPI, performs sentiment analysis on headlines, stores the processed data in AWS RDS PostgreSQL, and visualizes insights through a real-time Streamlit dashboard deployed on AWS ECS Fargate.

---

## 📌 Project Highlights

✅ Automated news ingestion using AWS Lambda  
✅ Scheduled execution with EventBridge  
✅ Real-time sentiment analytics dashboard  
✅ PostgreSQL RDS cloud database integration  
✅ Docker containerization  
✅ AWS ECS Fargate deployment  
✅ AWS ECR image management  
✅ Live cloud-hosted dashboard  
✅ End-to-end serverless cloud pipeline  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Streamlit | Dashboard UI |
| PostgreSQL RDS | Cloud Database |
| AWS Lambda | Serverless Processing |
| EventBridge | Scheduling Automation |
| Docker | Containerization |
| AWS ECR | Docker Image Registry |
| AWS ECS Fargate | Cloud Deployment |
| NewsAPI | Real-Time News Data |

---

## ☁️ Cloud Architecture

```text
EventBridge
    ↓
AWS Lambda
    ↓
News API
    ↓
PostgreSQL RDS
    ↓
Streamlit Dashboard
    ↓
Docker Container
    ↓
AWS ECS Fargate


---------------------------------------------

📊 Dashboard Features
Live News Feed
Sentiment Analysis
Positive / Negative Indicators
Real-Time Data Updates
Cloud-Based Deployment
Interactive Streamlit UI

---------------------------------------------

🎯 Project Objective

The main objective of this project is to demonstrate a complete real-time cloud data engineering pipeline using AWS services. The system automatically collects live news data, processes sentiment, stores it in a scalable cloud database, and displays analytics through an interactive dashboard.


----------------------------------------------

🌐 Deployment

The application is deployed using:

AWS ECS Fargate
Docker Containers
AWS ECR
AWS RDS PostgreSQL
AWS Lambda + EventBridge Automation

---------------------------------------------

📷 Final Output

Real-time cloud-hosted analytics dashboard with automated news ingestion and sentiment analysis.

---------------------------------------------


## 🌐 Live Dashboard

[Open Live Dashboard](http://13.204.73.76:8501)





