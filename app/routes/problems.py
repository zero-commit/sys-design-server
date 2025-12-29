from flask import Blueprint, request, jsonify
from app.services.problem_service import create_problem

problems_bp = Blueprint("problems", __name__)

@problems_bp.route("/api/v1/problems", methods=["POST"])
def create():
    data = request.json

    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    problem = create_problem(data)

    return jsonify({
        "id": problem.id,
        "title": problem.title,
        "difficulty": problem.difficulty
    }), 201
