from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    "Python uygulamasini yaz",
    "Azure Pipeline kur",
    "yeni versiyon"
]

@app.route("/")
def home():
    return "Mini Tasks API is running!"

@app.route("/tasks")
def list_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)