from app.extensions import db
import uuid

class Evaluation(db.Model):
    __tablename__ = "evaluations"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    submission_id = db.Column(db.String, db.ForeignKey("submissions.id"))
    scores = db.Column(db.JSON, nullable=False)
    final_score = db.Column(db.Float)
    reasoning = db.Column(db.Text)
