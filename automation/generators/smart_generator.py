import os
from automation.generators.groq_generator import GroqGenerator


class SmartGenerator:

    def __init__(self):

        self.primary = GroqGenerator(model="llama3-70b-8192")

        # 🔥 fallback sempre disponibile
        self.fallback_enabled = True

    # -------------------------
    # GENERATE
    # -------------------------

    def generate(self, prompt):

        print("🧠 AI PRIMARY (GROQ)...")

        try:

            result = self.primary.generate(prompt)

            # 🔥 VALIDAZIONE OUTPUT
            if not result or len(str(result).strip()) < 50:
                raise Exception("Risposta troppo corta o vuota")

            return result

        except Exception as e:

            print(f"⚠️ GROQ FAILED: {e}")

            if self.fallback_enabled:
                return self.fallback(prompt)

            raise

    # -------------------------
    # FALLBACK SICURO
    # -------------------------

    def fallback(self, prompt):

        print("🧱 USING FALLBACK TEMPLATE")

        # 🔥 fallback leggermente più realistico
        return """
<h1>Come imparare una lingua in modo efficace</h1>

<p>Imparare una lingua richiede costanza, esposizione quotidiana e pratica reale.</p>

<h2>1. Esporsi alla lingua ogni giorno</h2>
<p>Anche 10-15 minuti al giorno fanno la differenza.</p>

<h2>2. Parlare fin da subito</h2>
<p>Non aspettare la perfezione: usa la lingua subito.</p>

<h2>3. Metodo consigliato</h2>
<p>Strumenti come Babbel aiutano a costruire una base solida.</p>

<p><strong>Consiglio:</strong> la continuità è più importante della quantità.</p>
"""
