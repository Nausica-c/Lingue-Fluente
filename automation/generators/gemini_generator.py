import os
import requests


class GeminiGenerator:

    def __init__(self, model="gemini-1.5-flash"):

        self.model = model

        # 🔥 LEGGE LA KEY DA ENV (GitHub Secrets)
        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise Exception("❌ GEMINI_API_KEY non trovata nelle environment variables")

        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"

    # -------------------------
    # CALL AI
    # -------------------------

    def generate(self, prompt):

        headers = {
            "Content-Type": "application/json"
        }

        params = {
            "key": self.api_key
        }

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        response = requests.post(
            self.endpoint,
            headers=headers,
            params=params,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            raise Exception(f"Errore API Gemini: {response.text}")

        data = response.json()

        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            raise Exception(f"Risposta Gemini non valida: {data}")

    # -------------------------
    # DEBUG TEST
    # -------------------------

    def test(self):
        return self.generate("Scrivi una frase semplice per imparare inglese.")
