# 🚀 Real-Time News Sentiment Analytics Dashboard

## 📖 Project Overview

The Real-Time News Sentiment Analytics Dashboard is an end-to-end cloud-native data engineering project that automatically collects live news articles from NewsAPI, performs sentiment analysis using TextBlob, stores the processed data in AWS RDS PostgreSQL, and visualizes insights through an interactive Streamlit dashboard.

This project demonstrates real-world data engineering concepts including:

* Real-Time Data Collection
* Sentiment Analysis
* Cloud Database Integration
* Serverless Computing
* Dashboard Development
* Containerization
* Cloud Deployment
* Automated Scheduling

---

# 🎯 Project Objectives

The main objectives of this project are:

* Collect live news articles automatically
* Analyze news sentiment in real time
* Store processed data in a scalable cloud database
* Visualize insights through an interactive dashboard
* Automate workflows using AWS services
* Deploy cloud-native applications using Docker and ECS

---

# 🛠️ Technologies Used

| Technology           | Purpose                 |
| -------------------- | ----------------------- |
| Python               | Application Development |
| NewsAPI              | News Data Source        |
| TextBlob             | Sentiment Analysis      |
| PostgreSQL (AWS RDS) | Cloud Database          |
| Streamlit            | Dashboard Development   |
| AWS Lambda           | Serverless Processing   |
| EventBridge          | Scheduled Automation    |
| Docker               | Containerization        |
| AWS ECR              | Container Registry      |
| AWS ECS Fargate      | Cloud Deployment        |
| Git & GitHub         | Version Control         |

---

# ☁️ Architecture Flow

```text
┌─────────────────┐
│  EventBridge    │
│ Scheduled Job   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ AWS Lambda      │
│ Data Collector  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ NewsAPI         │
│ Live News Data  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ TextBlob        │
│ Sentiment       │
│ Analysis        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ AWS RDS         │
│ PostgreSQL      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Streamlit       │
│ Dashboard       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Docker          │
│ Container       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ AWS ECS         │
│ Fargate         │
└─────────────────┘
```

---

# 📂 Project Structure

```text
news-analytics-dashboard/
│
├── fetch_news.py
├── test_db.py
├── dashboard.py
├── lambda_function.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# 🔄 Project Workflow

### Step 1 – Fetch News Data

News articles are collected from NewsAPI based on predefined keywords such as:

* AI
* Technology
* Cloud Computing

Output:

* JSON formatted news data

---

### Step 2 – Perform Sentiment Analysis

TextBlob calculates sentiment polarity for each news headline.

Example:

```text
"AI Innovation Reaches New Heights"
```

Output:

```text
Sentiment Score = 0.75
Sentiment Label = Positive
```

---

### Step 3 – Store Processed Data

Processed records are stored in PostgreSQL.

Stored Fields:

* News Date
* Source Name
* News Title
* Sentiment Score
* Sentiment Label
* Created Timestamp

---

### Step 4 – Dashboard Visualization

Streamlit reads data from PostgreSQL and displays:

* News Headlines
* Sentiment Scores
* Sentiment Labels
* Latest Update Timestamp

---

# 📄 File Documentation

## 1. fetch_news.py

### Purpose

Collects live news data, performs sentiment analysis, and stores processed records in PostgreSQL.

### Code Usage

#### Import Libraries

```python
import requests
import psycopg2
from textblob import TextBlob
from datetime import datetime
```

Purpose:

* requests → Fetch data from NewsAPI
* psycopg2 → PostgreSQL connection
* TextBlob → Sentiment Analysis
* datetime → Date conversion

#### Environment Variables

```python
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
```

Purpose:

* Securely loads API credentials

#### Database Connection

```python
conn = psycopg2.connect(...)
```

Purpose:

* Connects application to AWS RDS PostgreSQL

#### Fetch News

```python
response = requests.get(...)
```

Purpose:

* Retrieves live news articles

#### Sentiment Analysis

```python
TextBlob(title).sentiment.polarity
```

Purpose:

* Calculates sentiment score
* Determines Positive, Negative, or Neutral sentiment

#### Store Data

```python
cur.execute(...)
```

Purpose:

* Inserts processed records into PostgreSQL

---

## 2. test_db.py

### Purpose

Creates and validates the PostgreSQL database schema.

### Code Usage

#### Database Connection

```python
psycopg2.connect(...)
```

Purpose:

* Tests PostgreSQL connectivity

#### Create Table

```sql
CREATE TABLE IF NOT EXISTS news_data
```

Purpose:

* Creates database table structure

#### Commit Changes

```python
conn.commit()
```

Purpose:

* Saves schema changes

---

## 3. dashboard.py

### Purpose

Provides an interactive dashboard for visualizing sentiment analytics.

### Code Usage

#### Streamlit Configuration

```python
st.set_page_config(...)
```

Purpose:

* Configures dashboard layout

#### Auto Refresh

```python
st_autorefresh(...)
```

Purpose:

* Refreshes dashboard automatically

#### Database Query

```python
pd.read_sql(...)
```

Purpose:

* Loads latest news records

#### Custom Styling

```python
st.markdown(...)
```

Purpose:

* Improves dashboard appearance

#### Sidebar Navigation

```python
st.sidebar.radio(...)
```

Purpose:

* Provides navigation controls

#### Sentiment Coloring

```python
def color_sentiment(value):
```

Purpose:

* Positive → Green
* Negative → Red
* Neutral → Gray

#### Data Display

```python
st.dataframe(...)
```

Purpose:

* Displays interactive analytics table

---

## 4. lambda_function.py

### Purpose

Automates news collection using AWS Lambda.

### Features

* Serverless execution
* Automated processing
* Scheduled data collection

---

## 5. Dockerfile

### Purpose

Containerizes the application for deployment.

### Benefits

* Consistent environment
* Easy deployment
* Cloud portability

---

## 6. requirements.txt

### Purpose

Defines project dependencies.

Example packages:

* streamlit
* pandas
* requests
* sqlalchemy
* psycopg2
* textblob
* python-dotenv

---

# 🗄️ Database Schema

### Table: news_data

| Column          | Description                   |
| --------------- | ----------------------------- |
| id              | Unique Record ID              |
| news_date       | News Publication Date         |
| source_name     | News Source                   |
| title           | News Headline                 |
| sentiment_score | Sentiment Score               |
| sentiment_label | Positive / Negative / Neutral |
| created_at      | Record Timestamp              |

---

# 📊 Dashboard Features

* Live News Feed
* Sentiment Analysis
* Positive / Negative Classification
* Automatic Data Refresh
* Interactive Streamlit Dashboard
* Cloud-Based Deployment

---

# 🚀 Deployment Architecture

Deployment Services:

* AWS Lambda
* EventBridge
* AWS RDS PostgreSQL
* Docker
* AWS ECR
* AWS ECS Fargate

Deployment Workflow:

```text
Application
    ↓
Docker Build
    ↓
AWS ECR
    ↓
AWS ECS Fargate
    ↓
Public Dashboard
```

---

# 🌐 Live Dashboard

http://13.204.73.76:8501

---

# 🔒 Security Features

Sensitive credentials are stored using environment variables.

Example:

```env
NEWS_API_KEY=your_api_key
DB_PASSWORD=your_password
```

`.env` is excluded using `.gitignore`.

---

# 🔧 Troubleshooting Guide

## NewsAPI Authentication Error

Error:

```text
401 Unauthorized
```

Solution:

* Verify NEWS_API_KEY
* Check .env configuration

---

## Database Connection Error

Error:

```text
connection refused
```

Solution:

* Verify RDS status
* Check Security Group rules
* Confirm PostgreSQL endpoint

---

## Table Does Not Exist

Error:

```text
relation "news_data" does not exist
```

Solution:

Run:

```bash
python test_db.py
```

---

## Dashboard Shows No Data

Solution:

Run:

```bash
python fetch_news.py
```

Verify:

```sql
SELECT * FROM news_data;
```

---

## Streamlit Not Loading

Run:

```bash
streamlit run dashboard.py
```

---

## Docker Build Failure

Verify:

```text
requirements.txt
```

contains all dependencies.

Rebuild:

```bash
docker build -t news-dashboard .
```

---

## Lambda Not Executing

Verify:

* EventBridge Schedule
* Lambda Permissions
* CloudWatch Logs

---

# 📈 Future Enhancements

* Interactive Charts
* Trend Analysis
* News Category Filters
* Snowflake Integration
* Real-Time Streaming Pipeline
* AI-Based News Summarization

---

# 👨‍💻 Author

**Karthik Sudhi**

Aspiring Data Engineer | AWS | PostgreSQL | Python | Streamlit | Docker

