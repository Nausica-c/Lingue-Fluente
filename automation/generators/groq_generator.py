import os
import requests


class GroqGenerator:

    def __init__(self, model="llama3-70b-8192"):

        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = model

        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def generate(self, prompt):

        if not self.api_key:
            raise Exception("GROQ_API_KEY mancante")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        r = requests.post(self.url, headers=headers, json=payload)

        if r.status_code != 200:
            raise Exception(r.text)

        return r.json()["choices"][0]["message"]["content"]
