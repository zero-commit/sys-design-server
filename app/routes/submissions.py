from flask import Blueprint, request, jsonify
from app.services.submission_service import create_submission

bp = Blueprint("submissions", __name__)

@bp.route("/api/v1/submissions", methods=["POST"])
def submit():
    submission = create_submission(request.json)
    return jsonify({"submission_id": submission.id})
