from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.json
    text = data.get("message", "")

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    score = int((polarity + 1) * 50)

    if score >= 70:
        status = "Stable"
    elif score >= 40:
        status = "Stressed"
    else:
        status = "Critical"

    emergency_words = ["suicide", "kill myself", "end it", "give up", "die"]
    is_emergency = any(word in text.lower() for word in emergency_words)

    return jsonify({
        "score": score,
        "status": status,
        "emergency": is_emergency
    })

if __name__ == "__main__":
    app.run(debug=True)
