import os
from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "postgres"),
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )

@app.route("/")
def home():
    return "Hello DevOps 🚀"

@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return "OK", 200
    except Exception as e:
        return "DB ERROR", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
