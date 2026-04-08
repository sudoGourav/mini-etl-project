FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install pandas psycopg2-binary

CMD ["bash"]