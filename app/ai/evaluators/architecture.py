from .base import BaseEvaluator

class ArchitectureEvaluator(BaseEvaluator):
    def evaluate(self, problem, code):
        prompt = f"""
You are a senior distributed systems interviewer.

TASK:
Evaluate ONLY SYSTEM ARCHITECTURE.

STRICTLY DO NOT evaluate:
- Code syntax
- Algorithm efficiency
- Minor implementation details

Focus ONLY on:
- Component separation
- Responsibility boundaries
- Deployment assumptions
- Where this system logically lives (gateway, service, worker, etc.)

Problem Description:
{problem}

Solution Code:
{code}

SCORING RULES:
Return ONE value only from:
0.0, 0.25, 0.5, 0.75, 1.0

Return JSON ONLY:
{{
  "architecture": float,
  "summary": string
}}

Summary rules:
- 2-3 sentences max
- Explain WHY the score was given
- Focus on system structure, not code details
"""
        return self.client.evaluate(prompt)
