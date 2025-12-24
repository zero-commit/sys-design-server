from app.models.submission import Submission
from app.extensions import db

def create_submission(data):
    submission = Submission(
        problem_id=data["problem_id"],
        prompts=data["prompts"],
        solution_code=data["solution_code"],
        language=data.get("language", "python")
    )
    db.session.add(submission)
    db.session.commit()
    return submission
