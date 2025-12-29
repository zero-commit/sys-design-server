import uuid
from app.extensions import db
from app.models.problem import Problem


def create_problem(data: dict) -> Problem:
    problem = Problem(
        id=str(uuid.uuid4()),
        title=data["title"],
        description=data["description"],
        difficulty=data.get("difficulty", "medium")
    )

    db.session.add(problem)
    db.session.commit()

    return problem
