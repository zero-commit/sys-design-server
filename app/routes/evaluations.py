from flask import Blueprint, jsonify
from app.services.evaluation_service import evaluate_submission

bp = Blueprint("evaluations", __name__)

@bp.route("/api/v1/evaluations/<submission_id>", methods=["POST"])
def evaluate(submission_id):
    result = evaluate_submission(submission_id)
    return jsonify(result)
