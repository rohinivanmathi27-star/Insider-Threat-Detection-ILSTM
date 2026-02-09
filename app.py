from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Insider Threat Detection System is Running"

@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    activity = data.get("activity")

    if not activity:
        return jsonify({"error": "No activity data"}), 400

    score = sum(activity) / len(activity)
    trust = round(1 - (score / 10), 2)

    status = "Normal" if trust > 0.6 else "Suspicious"

    return jsonify({
        "trust_score": trust,
        "status": status
    })

if __name__ == "__main__":
    app.run(debug=True)
