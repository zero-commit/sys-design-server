MAX_CHARS = 20000

def summarize_code_if_needed(client, code: str) -> str:
    if len(code) <= MAX_CHARS:
        return code

    prompt = f"""
Summarize this code into:
- components
- data models
- responsibilities
- scalability assumptions

DO NOT include line-by-line logic.

Code:
{code[:25000]}
"""
    try:
        summary = client.generate_text(prompt)
        return f"SUMMARY:\n{summary}"
    except Exception:
        return code[:15000] + "\n...[TRUNCATED]..."
