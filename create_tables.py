from app import create_app
from app.extensions import db
from app.models.problem import Problem
from app.models.submission import Submission
from app.models.evaluation import Evaluation

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables created successfully")
