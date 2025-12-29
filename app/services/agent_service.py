import json
from app.ai.agent_prompt import build_agent_prompt
from app.ai.gemini_client import GeminiClient
from config import Config


MAX_CODE_CHARS = 12000
MAX_HISTORY_TURNS = 5

def parse_agent_response(text: str):
    # Remove ```json fences if present
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return {
            "reply": text,
            "patch": None
        }

    return {
        "reply": parsed.get("reply", ""),
        "patch": parsed.get("patch")
    }

def handle_agent_chat(message, current_code, problem, history):
    client = GeminiClient(api_key=Config.GEMINI_API_KEY)

    # ---- Token safety ----
    safe_code = current_code[:MAX_CODE_CHARS]
    safe_history = history[-MAX_HISTORY_TURNS:]

    prompt = build_agent_prompt(
        message=message,
        code=safe_code,
        problem=problem,
        history=safe_history
    )

    raw_response = client.generate_text(prompt)

    return parse_agent_response(raw_response)
