from app.extensions import db
import uuid

class Submission(db.Model):
    __tablename__ = "submissions"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    problem_id = db.Column(db.String, db.ForeignKey("problems.id"))
    prompts = db.Column(db.JSON, nullable=False)
    solution_code = db.Column(db.Text, nullable=False)
    language = db.Column(db.String)
