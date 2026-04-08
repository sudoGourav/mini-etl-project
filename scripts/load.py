import psycopg2
import pandas as pd

# Load data
df = pd.read_csv("data/netflix.csv")

# Cleaning
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df = df.dropna(subset=['date_added', 'rating', 'duration'])
df = df.drop_duplicates()

# Connect DB
conn = psycopg2.connect(
    host="db",
    database="netflix_db",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS netflix (
    show_id TEXT PRIMARY KEY,
    type TEXT,
    title TEXT,
    director TEXT,
    cast_members TEXT,
    country TEXT,
    date_added TIMESTAMP,
    release_year INT,
    rating TEXT,
    duration TEXT,
    listed_in TEXT,
    description TEXT
);
""")

# Insert data
for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO netflix (
        show_id, type, title, director, cast_members,
        country, date_added, release_year, rating,
        duration, listed_in, description
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (show_id) DO NOTHING;
    """, (
        row['show_id'],
        row['type'],
        row['title'],
        row['director'],
        row['cast'],
        row['country'],
        row['date_added'],
        row['release_year'],
        row['rating'],
        row['duration'],
        row['listed_in'],
        row['description']
    ))

conn.commit()
cur.close()
conn.close()

print("✅ Data loaded into PostgreSQL!")