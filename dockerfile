# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install pandas psycopg2-binary

# Default command
CMD ["bash"]