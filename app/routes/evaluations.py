from flask import Blueprint, jsonify
from app.services.evaluation_service import evaluate_submission

evaluations_bp = Blueprint("evaluations", __name__)

@evaluations_bp.route("/v1/evaluations/<submission_id>", methods=["POST"])
def evaluate(submission_id):
    evaluation = evaluate_submission(submission_id)
    return jsonify({
        "evaluation_id": evaluation.id,
        "final_score": evaluation.final_score,
        "scores": evaluation.scores,
        "reasoning": evaluation.reasoning
    })
