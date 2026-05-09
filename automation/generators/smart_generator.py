import os
from automation.generators.groq_generator import GroqGenerator


class SmartGenerator:

    def __init__(self):

        self.primary = GroqGenerator(model="llama3-70b-8192")

    def generate(self, prompt):

        try:
            print("🧠 AI PRIMARY (GROQ)...")
            return self.primary.generate(prompt)

        except Exception as e:

            print(f"⚠️ GROQ FAILED: {e}")

            return self.fallback(prompt)

    # -------------------------
    # FALLBACK SICURO
    # -------------------------

    def fallback(self, prompt):

        print("🧱 USING FALLBACK TEMPLATE")

        return f"""
# Articolo generato automaticamente

Questo contenuto è una versione semplificata generata dal sistema.

## Contenuto base

Imparare una lingua richiede costanza e pratica quotidiana.

Esempi pratici aiutano molto nella memorizzazione.

👉 Usa Babbel per migliorare in modo strutturato.

(Autopilot fallback mode)
"""
