import json
from financial_assistant.services.openai_service import ask_openai


def generate_portfolio(req):
    prompt = f"""
You are a financial assistant tasked with generating investment portfolio recommendations.

The user has provided the following details:
- Budget: {req.budget}
- Risk: {req.risk}
- Investment Horizon: {req.horizon}

Your task is to recommend a portfolio based on the user's risk tolerance, budget, and investment horizon. Select appropriate ETFs dynamically and return ONLY valid JSON in the following format:
{{
  "risk": "{req.risk}",
  "portfolio": [
    {{
      "ticker": "DYNAMICALLY SELECTED TICKER",
      "allocation_percent": 100,
      "reason": "Explain why this ticker was selected based on the user's input."
    }}
  ],
  "summary": "Provide a summary of the recommendation."
}}

Do not include any additional text, explanations, or formatting outside of the JSON structure.
"""

    response = ask_openai(prompt)

    if not response:
        return {
            "error": "Empty response from OpenAI API",
            "raw": response,
            "fallback": {
                "risk": req.risk,
                "portfolio": [
                    {
                        "ticker": "VEQT",
                        "allocation_percent": 100,
                        "reason": "Fallback portfolio due to empty response"
                    }
                ],
                "summary": "Fallback response generated."
            }
        }

    try:
        # Validate and parse the JSON response
        return json.loads(response)
    except json.JSONDecodeError as e:
        # Return detailed error information
        return {
            "error": "Invalid JSON",
            "raw": response,
            "details": str(e)
        }
    except Exception as e:
        # Handle unexpected errors
        return {
            "error": "Unexpected error",
            "details": str(e)
        }