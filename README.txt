# 📊 Mini ETL Data Pipeline using Python, PostgreSQL & Docker

## 🚀 Project Overview

This project demonstrates a basic end-to-end ETL (Extract, Transform, Load) pipeline.
The pipeline processes a real-world dataset, cleans it, and loads it into a PostgreSQL database for analysis.

---

## 🧠 Architecture

```
CSV Dataset → Pandas (Cleaning & Transformation) → PostgreSQL → SQL Analysis
                 ↓
               Docker (Containerized Environment)
```

---

## ⚙️ Tech Stack

* **Python**
* **Pandas**
* **PostgreSQL**
* **Docker & Docker Compose**
* **SQL (PostgreSQL)**

---

## 📂 Project Structure

```
mini-etl-project/
│
├── data/
│   └── netflix.csv
│
├── scripts/
│   ├── clean.py
│   └── load.py
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🔧 Features

* Data cleaning using Pandas:

  * Handled missing values
  * Removed duplicates
  * Converted date formats
* Designed PostgreSQL schema for structured storage
* Loaded cleaned data into database using Python (psycopg2)
* Used Docker to containerize both application and database
* Performed SQL queries for validation and analysis

---

## 📊 Dataset

* Netflix Movies and TV Shows Dataset (Kaggle)
* ~8800 records processed

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/sudoGourav/mini-etl-project
cd mini-etl-project
```

### 2. Start services

```
docker-compose up --build
```

### 3. Run ETL pipeline

```
docker exec -it etl-app bash
python scripts/load.py
```

---

## 📈 Sample SQL Queries

### Count total records

```
SELECT COUNT(*) FROM netflix;
```

### Movies vs TV Shows

```
SELECT type, COUNT(*) 
FROM netflix 
GROUP BY type;
```

### Top countries

```
SELECT country, COUNT(*) 
FROM netflix 
GROUP BY country 
ORDER BY COUNT(*) DESC 
LIMIT 5;
```

---

## ✅ Results

* Cleaned dataset reduced from 8807 → ~8700 records
* Successfully loaded data into PostgreSQL
* Verified data integrity using SQL queries

---

## 🎯 Key Learnings

* Building ETL pipelines using Python
* Data cleaning and preprocessing techniques
* Working with PostgreSQL using psycopg2
* Docker-based environment setup
* Writing analytical SQL queries

---

## 🔥 Future Improvements

* Automate pipeline using Apache Airflow
* Add real-time data ingestion (API-based)
* Connect to Power BI / Tableau for visualization
* Optimize bulk inserts for better performance

---

## 👨‍💻 Author

* Gourav
* B.Tech CSE Student | Aspiring Data Engineer
