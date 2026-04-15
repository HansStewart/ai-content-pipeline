import os
from flask import Blueprint, request, jsonify, send_from_directory
from app.content_pipeline import run_content_pipeline

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), ".."), "index.html")

@main.route("/generate", methods=["POST"])
def generate_content():
    data = request.get_json()

    topic = data.get("topic")
    audience = data.get("audience")
    tone = data.get("tone")

    if not topic or not audience or not tone:
        return jsonify({
            "error": "Missing required fields: topic, audience, tone"
        }), 400

    result = run_content_pipeline(topic, audience, tone)

    return jsonify({
        "success": True,
        "inputs": {
            "topic": topic,
            "audience": audience,
            "tone": tone
        },
        "content_package": result
    })