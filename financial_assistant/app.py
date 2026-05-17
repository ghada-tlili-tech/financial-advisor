# app.py

import openai
from financial_assistant.etf_recommendation import ETFRecommendation

class FinancialAssistantApp:
    def __init__(self):
        self.api_key = "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"  # Replace with your OpenAI API key
        openai.api_key = self.api_key

    def run(self):
        # Get user inputs
        try:
            budget = float(input("Enter your budget (CAD): "))
            risk = input("Enter your risk level (low, medium, high): ").strip().lower()
            horizon = int(input("Enter your investment horizon (years): "))

            if risk not in ["low", "medium", "high"]:
                raise ValueError("Invalid risk level. Choose from: low, medium, high.")

            etf_recommendation = ETFRecommendation(budget, risk, horizon, self.api_key)
            portfolio = etf_recommendation.generate_portfolio()

            print(portfolio)
        except ValueError as e:
            print(f"Error: {e}")

    def query_openai(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return {"error": str(e)}