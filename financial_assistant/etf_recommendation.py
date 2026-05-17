# etf_recommendation.py

import json
import openai

class ETFRecommendation:
    def __init__(self, budget, risk, horizon, api_key):
        self.budget = budget
        self.risk = risk
        self.horizon = horizon
        self.api_key = api_key

    def generate_portfolio(self):
        openai_response = self.query_openai_for_portfolio()
        if isinstance(openai_response, dict):
            return openai_response
        try:
            portfolio = json.loads(openai_response)
            return portfolio
        except json.JSONDecodeError as e:
            return {"error": "Failed to parse OpenAI response as JSON.", "details": str(e)}

    def query_openai_for_portfolio(self):
        openai.api_key = self.api_key
        prompt = (
            f"You are a financial assistant. Based on the following inputs, recommend an ETF portfolio:\n"
            f"Budget: {self.budget} CAD\n"
            f"Risk: {self.risk}\n"
            f"Horizon: {self.horizon} years\n"
            f"Return the response in JSON format with the following structure:\n"
            f"{{\n"
            f"  \"risk\": \"...\",\n"
            f"  \"portfolio\": [\n"
            f"    {{\n"
            f"      \"ticker\": \"...\",\n"
            f"      \"allocation_percent\": 0,\n"
            f"      \"reason\": \"...\"\n"
            f"    }}\n"
            f"  ],\n"
            f"  \"summary\": \"...\"\n"
            f"}}"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return {"error": "An error occurred while querying OpenAI", "details": str(e)}

    def fetch_etf_data(self):
        # Placeholder for fetching ETF data (e.g., from an API or database)
        return []

    def allocate_portfolio(self, etf_data):
        # Placeholder allocation logic based on risk and horizon
        if self.risk == "low":
            return [
                {"ticker": "ETF1", "allocation_percent": 70, "reason": "Low risk preference."},
                {"ticker": "ETF2", "allocation_percent": 30, "reason": "Moderate growth potential."}
            ]
        elif self.risk == "medium":
            return [
                {"ticker": "ETF2", "allocation_percent": 50, "reason": "Balanced risk and return."},
                {"ticker": "ETF3", "allocation_percent": 50, "reason": "Higher growth potential."}
            ]
        else:  # High risk
            return [
                {"ticker": "ETF3", "allocation_percent": 100, "reason": "Maximized growth potential."}
            ]