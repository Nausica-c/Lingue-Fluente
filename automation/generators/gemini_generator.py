import requests


class GeminiGenerator:

    def __init__(self, model="gemini-2.5-pro"):
        self.model = model

        # qui metterai la tua API key
        self.api_key = "INSERISCI_API_KEY"

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
            json=payload
        )

        if response.status_code != 200:
            raise Exception(f"Errore API Gemini: {response.text}")

        data = response.json()

        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            raise Exception("Risposta Gemini non valida o vuota")

    # -------------------------
    # OPTIONAL: DEBUG
    # -------------------------

    def test(self):
        return self.generate("Scrivi una frase semplice per imparare inglese.")
