from financial_assistant.core.etf_engine import generate_portfolio

class FinancialAssistantApp:
    def run(self):
        try:
            budget = float(input("Enter your budget (CAD): "))
            risk = input("Enter risk (low, medium, high): ").strip().lower()
            horizon = int(input("Enter horizon (years): "))

            if risk not in ["low", "medium", "high"]:
                raise ValueError("Risk must be low, medium, or high")

            request = type("Req", (), {
                "budget": budget,
                "risk": risk,
                "horizon": horizon
            })()

            portfolio = generate_portfolio(request)

            print("\n=== AI ETF RECOMMENDATION ===")
            print(portfolio)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    app = FinancialAssistantApp()
    app.run()