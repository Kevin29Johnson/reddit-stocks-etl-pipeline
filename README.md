# Reddit Stock Sentiment ETL Pipeline

An automated ETL pipeline that extracts stock sentiment data from Reddit's WallStreetBets subreddit, processes sentiment analysis, and delivers interactive analytics dashboards for investment insights.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.0+-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)


## 🏗️ Architecture Diagram

![Architecture Diagram](https://i.ibb.co/PGQBdHQN/Screenshot-2025-06-03-at-10-42-46-PM.png)

## 🚀 Project Overview

- **Developed automated ETL pipeline** using Apache Airflow to extract stock sentiment data from Reddit's WallStreetBets subreddit API with daily scheduled ingestion workflows
- **Implemented sentiment analysis processing** with Python and Pandas, transforming raw comment data into structured sentiment scores and stock mention frequencies stored in PostgreSQL
- **Built interactive analytics dashboards** using Plotly to visualize sentiment trends, comment volume patterns, and stock ticker popularity for data-driven investment insights

## 🚀 Features

- **Automated Data Extraction:** Daily scheduled ingestion from Reddit's WallStreetBets API
- **Sentiment Analysis:** Processing of comments with custom sentiment scoring algorithms
- **Data Storage:** Structured storage in PostgreSQL with optimized schema
- **Interactive Dashboards:** Plotly visualizations for trend analysis
- **Stock Tracking:** Monitor mention frequencies and sentiment for trending tickers
- **Scalable Pipeline:** Apache Airflow orchestration with error handling and monitoring

## 📊 Analytics & Insights

- **Sentiment Trends:** Track positive/negative sentiment patterns over time
- **Stock Popularity:** Most mentioned tickers in community discussions  
- **Comment Volume:** Daily activity patterns and engagement metrics
- **Market Correlation:** Analyze sentiment vs. stock price movements

## 🛠️ Technology Stack

- **Orchestration:** Apache Airflow
- **Data Processing:** Python, Pandas
- **Sentiment Analysis:** Custom Python analytics
- **Database:** PostgreSQL
- **Visualization:** Plotly
- **Containerization:** Docker
- **API:** Reddit WallStreetBets API 

## 📋 Prerequisites

- Python 3.8+
- Docker & Docker Compose
- PostgreSQL
- Reddit API credentials
- Apache Airflow
- Astro CLI

