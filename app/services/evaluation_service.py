import uuid
from app.extensions import db
from app.models.submission import Submission
from app.models.problem import Problem
from app.models.evaluation import Evaluation
from app.ai.gemini_client import GeminiClient
from app.ai.evaluators.architecture import ArchitectureEvaluator
from app.ai.evaluators.data_modelling import DataModelingEvaluator
from app.ai.evaluators.design_quality import DesignQualityEvaluator
from app.ai.evaluators.scalability import ScalabilityEvaluator
from app.ai.evaluators.prompt_alignment import PromptAlignmentEvaluator
from app.ai.summarizer import summarize_code_if_needed
from config import Config


def evaluate_submission(submission_id: str) -> Evaluation:
    """
    Evaluates a submission using GeminiClient.
    Handles large code by summarizing it first.
    """
    submission = Submission.query.get(submission_id)
    if not submission:
        raise ValueError("Submission not found")
    problem = Problem.query.get(submission.problem_id)
    if not problem:
        raise ValueError("Problem not found")

    client = GeminiClient(api_key=Config.GEMINI_API_KEY)

    # effective_code = submission.solution_code
    
    # # 20,000 chars is roughly 5k tokens. Good safety margin.
    # if len(effective_code) > 20000:
        
    #     summary_prompt = (
    #         f"Summarize the following code architecture, data models, and key functions "
    #         f"into a high-level technical summary. Focus on structure, not line-by-line details:\n\n"
    #         f"{effective_code[:25000]}" # Cap input to prevent recursive overflows
    #     )
        
    #     try:
    #         # Use the client's new helper method
    #         summary_text = client.generate_text(summary_prompt)
    #         effective_code = f"Summary of Solution Code:\n{summary_text}"
    #     except Exception as e:
    #         effective_code = effective_code[:15000] + "\n...[TRUNCATED]..."

    # # Update submission object temporarily (in memory only) for prompt building
    # submission.solution_code = effective_code
    # prompt = build_prompt(problem, submission)
    # scores = client.evaluate(prompt)

    code = summarize_code_if_needed(client, submission.solution_code)

    evaluators = [
        ArchitectureEvaluator(client),
        DataModelingEvaluator(client),
        DesignQualityEvaluator(client),
        ScalabilityEvaluator(client),
        PromptAlignmentEvaluator(client),
    ]

    results = {}
    summaries = []

    results.update(evaluators[0].evaluate(problem.description, code))
    results.update(evaluators[1].evaluate(problem.description, code))
    results.update(evaluators[2].evaluate(code))
    results.update(evaluators[3].evaluate(problem.description, code))
    results.update(evaluators[4].evaluate(problem.description, submission.prompts))

    for v in results.values():
        if isinstance(v, str):
            summaries.append(v)

    scores = {k: v for k, v in results.items() if isinstance(v, float)}
    final_score = round(sum(scores.values()) / len(scores), 2)

    evaluation = Evaluation(
        id=str(uuid.uuid4()),
        submission_id=submission.id,
        scores=scores,
        final_score=final_score,
        reasoning="\n".join(summaries)
    )

    db.session.add(evaluation)
    db.session.commit()
    return evaluation

