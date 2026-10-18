import os

import psycopg
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        dbname=os.getenv("DB_NAME", "minitasks"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "localdevpassword"),
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")

        return jsonify({"status": "healthy"}), 200

    except Exception:
        app.logger.exception("Health check failed")
        return jsonify({"status": "unhealthy"}), 503


@app.route("/tasks", methods=["GET", "POST"])
def tasks_api():
    if request.method == "GET":
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, title FROM tasks ORDER BY id")
                tasks = [
                    {"id": row[0], "title": row[1]}
                    for row in cur.fetchall()
                ]

        return jsonify(tasks), 200

    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Görev boş olamaz."}), 400

    if len(title) > 200:
        return jsonify(
            {"error": "Görev en fazla 200 karakter olabilir."}
        ), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title",
                (title,),
            )
            task_id, task_title = cur.fetchone()

    return jsonify({"id": task_id, "title": task_title}), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM tasks WHERE id = %s RETURNING id",
                (task_id,),
            )
            deleted = cur.fetchone()

    if deleted is None:
        return jsonify({"error": "Görev bulunamadı."}), 404

    return jsonify(
        {"message": "Görev silindi.", "id": task_id}
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)