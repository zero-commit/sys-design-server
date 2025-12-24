from app.models.submission import Submission
from app.models.problem import Problem
from app.models.evaluation import Evaluation
from app.extensions import db
from app.ai.prompt_builder import build_prompt
from app.ai.gemini_client import GeminiClient
from app.utils.scoring import aggregate_score

def evaluate_submission(submission_id):
    submission = Submission.query.get(submission_id)
    problem = Problem.query.get(submission.problem_id)

    prompt = build_prompt(problem, submission)

    client = GeminiClient()
    scores = client.evaluate(prompt)

    final = aggregate_score(scores)

    evaluation = Evaluation(
        submission_id=submission_id,
        scores=scores,
        final_score=final,
        reasoning=scores.get("summary")
    )

    db.session.add(evaluation)
    db.session.commit()

    return {
        "final_score": final,
        "scores": scores
    }
