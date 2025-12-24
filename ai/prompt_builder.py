def build_prompt(problem, submission):
    return f"""
Problem:
{problem.description}

Prompts Used:
{submission.prompts}

Solution Code:
{submission.solution_code}

Evaluate architecture, naming, scalability, and prompt alignment.
Return JSON only.
"""
