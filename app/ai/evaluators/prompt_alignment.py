from .base import BaseEvaluator

class PromptAlignmentEvaluator(BaseEvaluator):
    def evaluate(self, problem, prompts):
        prompt = f"""
        EVALUATE USER STRATEGY (SYSTEM DESIGN)

        [PROBLEM]
        {problem}

        [USER INTERACTION HISTORY]
        {prompts}

        [TASK]
        Score the USER'S ability to guide the system design. Ignore the final code.
        Focus on:
        1. Signal-to-Noise: Did they ask for specific components (e.g., "Redis") vs generic requests ("make it fast")?
        2. Constraint Handling: Did they address specific bottlenecks defined in the problem?
        3. Iteration: Did subsequent prompts refine the architecture or just repeat requests?

        [SCORING]
        1.0: Optimal. User identified key constraints and explicitly requested correct components.
        0.7: Good. User understood the flow but missed optimization details.
        0.5: Generic. "Build a chat app" level depth. No architectural specificities.
        0.2: Poor. Misguided or irrelevant requests.

        [OUTPUT]
        Return JSON ONLY: {{ "prompt_alignment": float, "summary": "Concise critique of user strategy." }}
        """
        return self.client.evaluate(prompt)