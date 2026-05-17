import json
from financial_assistant.services.openai_service import ask_openai


def generate_portfolio(req):
    prompt = f"""
You are a financial assistant.

Budget: {req.budget}
Risk: {req.risk}
Horizon: {req.horizon}

Return ONLY valid JSON:
{{
  "risk": "{req.risk}",
  "portfolio": [
    {{
      "ticker": "VEQT",
      "allocation_percent": 100,
      "reason": "simple test portfolio"
    }}
  ],
  "summary": "test response"
}}
"""

    response = ask_openai(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {"error": "Invalid JSON", "raw": response}