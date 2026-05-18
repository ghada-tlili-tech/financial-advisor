from openai import OpenAI
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(prompt: str):
    try:
        logging.info("Sending request to OpenAI API with prompt: %s", prompt)
        response = client.responses.create(
            model="gpt-4",  # Switched to a more robust model
            input=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_output_tokens=200
        )
        logging.info("Received response metadata: %s", response.metadata)
        logging.info("Received response text: %s", response.output_text)
        return response.output_text
    except TypeError as e:
        logging.error("TypeError during API call: %s", str(e))
        return f"Error: Invalid API call - {str(e)}"
    except Exception as e:
        logging.error("Unexpected error during API call: %s", str(e))
        return f"Error: Unexpected error - {str(e)}"