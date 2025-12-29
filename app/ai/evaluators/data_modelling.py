from .base import BaseEvaluator

class DataModelingEvaluator(BaseEvaluator):
    def evaluate(self, problem, code):
        prompt = f"""
You are evaluating data modeling and interfaces for a system design.

TASK:
Evaluate ONLY DATA MODELING & INTERFACES.

STRICTLY DO NOT evaluate:
- Overall architecture
- Scalability strategies
- Code performance

Focus ONLY on:
- Data structures used
- State representation
- Interfaces between components
- Appropriateness of models for the problem

Problem Description:
{problem}

Solution Code:
{code}

SCORING RULES:
Return ONE value only from:
0.0, 0.25, 0.5, 0.75, 1.0

Return JSON ONLY:
{{
  "data_modeling": float,
  "summary": string
}}

Summary rules:
- 2-3 sentences
- Explain strengths and gaps in modeling
"""
        return self.client.evaluate(prompt)
