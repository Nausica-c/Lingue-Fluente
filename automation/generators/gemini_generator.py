import os
import requests


class GeminiGenerator:

    def __init__(self, model="gemini-pro"):

        self.model = model

        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise Exception("❌ GEMINI_API_KEY mancante")

        self.endpoint = (
            f"https://generativelanguage.googleapis.com/v1beta/"
            f"models/{self.model}:generateContent"
        )

    def generate(self, prompt):

        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(
            self.endpoint,
            params={"key": self.api_key},
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            raise Exception(f"Errore API Gemini: {response.text}")

        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]
