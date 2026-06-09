import requests
import psycopg2
from textblob import TextBlob
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

api_key = "YOUR_API_KEY""

api_key = os.getenv("NEWS_API_KEY")

conn = psycopg2.connect(
    host="news-db.czasscka2fsx.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    port="5432"
)
print(conn.get_dsn_parameters())


cur = conn.cursor()

url = "https://newsapi.org/v2/everything"

params = {
    "q": "AI OR technology OR cloud",
    "language": "en",
    "pageSize": 20,
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

articles = response.json().get("articles", [])

print("Number of articles:", len(articles))

for article in articles:

    title = article.get("title")

    source_name = article.get("source", {}).get("name")

    published_at = article.get("publishedAt")

    if published_at:
        news_date = datetime.strptime(
            published_at,
            "%Y-%m-%dT%H:%M:%SZ"
        ).date()
    else:
        news_date = None

#     sentiment_score = TextBlob(title).sentiment.polarity

#     if sentiment_score > 0:
#         sentiment_label = "Positive"
#     elif sentiment_score < 0:
#         sentiment_label = "Negative"
#     else:
#         sentiment_label = "Neutral"
        

#     cur.execute("""
#         INSERT INTO news_data
#         (
#             news_date,
#             source_name,
#             title,
#             sentiment_score,
#             sentiment_label
#         )
#         VALUES (%s, %s, %s, %s, %s)
#     """, (
#         news_date,
#         source_name,
#         title,
#         sentiment_score,
#         sentiment_label
#     ))

# conn.commit()

# print("Data inserted successfully!")

# cur.close()
# conn.close()