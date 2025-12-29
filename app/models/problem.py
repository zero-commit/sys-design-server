from app.extensions import db
import uuid

class Problem(db.Model):
    __tablename__ = "problems"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
