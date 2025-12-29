from flask import Blueprint, request, jsonify
from app.services.agent_service import handle_agent_chat

agent_bp = Blueprint("agent", __name__, url_prefix="/api/v1/agent")


@agent_bp.route("/chat", methods=["POST"])
def chat_with_agent():
    data = request.get_json()

    reply = handle_agent_chat(
        message=data["message"],
        current_code=data["current_code"],
        problem=data["problem_description"],
        history=data.get("history", [])
    )

    return jsonify(reply), 200
