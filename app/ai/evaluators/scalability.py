from .base import BaseEvaluator

class ScalabilityEvaluator(BaseEvaluator):
    def evaluate(self, problem, code):
        prompt = f"""
You are a senior system design interviewer.

TASK:
Evaluate ONLY SCALABILITY AWARENESS.

STRICTLY DO NOT evaluate:
- Local correctness
- Code style
- Naming or formatting

Focus ONLY on:
- Multi-instance behavior
- Shared state handling
- Bottlenecks
- Horizontal scaling readiness

Problem Description:
{problem}

Solution Code:
{code}

SCORING RULES:
Return ONE value only from:
0.0, 0.25, 0.5, 0.75, 1.0

Return JSON ONLY:
{{
  "scalability": float,
  "summary": string
}}

Summary rules:
- Be direct and critical
- 2-3 sentences max
"""
        return self.client.evaluate(prompt)

