from flask import Blueprint, request, jsonify
from app.content_pipeline import run_content_pipeline

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "AI Content Pipeline Agent",
        "powered_by": "CrewAI + GPT-4o",
        "endpoints": {
            "POST /generate": "Generate email, LinkedIn post, blog outline, and ad copy"
        }
    })

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