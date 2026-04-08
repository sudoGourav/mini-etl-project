import pandas as pd

df = pd.read_csv("data/netflix.csv")

print("Before Cleaning:")
print(df.isnull().sum())

# Fill non-critical columns
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")

# Convert date FIRST
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Now drop critical nulls
df = df.dropna(subset=['date_added', 'rating', 'duration'])

# Remove duplicates
df = df.drop_duplicates()

print("\nAfter Cleaning:")
print(df.isnull().sum())

print("\nTotal rows after cleaning:", len(df))