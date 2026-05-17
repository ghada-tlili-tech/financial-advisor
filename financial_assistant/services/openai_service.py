from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

def ask_openai(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a financial assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content