import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from financial_assistant.app import FinancialAssistantApp

if __name__ == "__main__":
    app = FinancialAssistantApp()
    app.run()