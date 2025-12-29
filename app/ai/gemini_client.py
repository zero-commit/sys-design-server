import json
import re
from google import genai

class GeminiClient:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def generate_text(self, prompt: str) -> str:
        print("Tokens used in evaluating prompt", len(prompt.split()))
        return self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={"temperature": 0.2}
            ).text

    def evaluate(self, prompt: str) -> dict:
        raw = self.generate_text(prompt)
        cleaned = re.sub(r"```json|```", "", raw).strip()
        return json.loads(cleaned)
