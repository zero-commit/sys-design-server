from .base import BaseEvaluator

class DesignQualityEvaluator(BaseEvaluator):
    def evaluate(self, code):
        prompt = f"""
You are reviewing code quality from a system design interview perspective.

TASK:
Evaluate ONLY DESIGN QUALITY.

STRICTLY DO NOT evaluate:
- Architecture decisions
- Scalability or distribution
- Algorithm correctness

Focus ONLY on:
- Modularity
- Naming clarity
- Separation of concerns
- Readability and extensibility
Solution Code:
{code}

SCORING RULES:
Return ONE value only from:
0.0, 0.25, 0.5, 0.75, 1.0

Return JSON ONLY:
{{
  "design_quality": float,
  "summary": string
}}

Summary rules:
- 2 sentences max
- Mention what makes the code easy or hard to extend
"""
        return self.client.evaluate(prompt)
