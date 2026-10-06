from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "CareerHub Backend is running successfully!"


@app.route("/api/career")
def career():
    return jsonify({
        "career": "Data Scientist",
        "readiness_score": 75,
        "skills": [
            "Python",
            "SQL",
            "Machine Learning",
            "Pandas"
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)