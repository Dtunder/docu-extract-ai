import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def extract_document(pages: list[str], doc_type: str = "auto") -> dict:
    mock_llm = os.environ.get("MOCK_LLM", "false").lower() == "true"

    if mock_llm:
        if doc_type == "contract":
            return {
                "parties": ["Muster GmbH", "Tech Solutions AG"],
                "date": "01.10.2023",
                "value": "50.000,00 €",
                "terms": "Netto 30 Tage"
            }
        else:
            return {
                "vendor": "Muster GmbH",
                "date": "15.05.2024",
                "amount": "1.234,56 €",
                "iban": "DE12345678901234567890",
                "line_items": [
                    {"description": "Web Development", "quantity": "1", "price": "1.000,00 €"},
                    {"description": "Hosting", "quantity": "12", "price": "234,56 €"}
                ]
            }

    # Use Gemini API
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set")

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        full_text = "\n".join(pages)

        if doc_type == "contract":
            prompt = f"""
            Extract the following information from this German contract text:
            - parties (list of strings)
            - date
            - value
            - terms

            Return the output strictly as a JSON object matching this structure.
            If a field is not found, return null for it.

            Text:
            {full_text}
            """
        else:
            prompt = f"""
            Extract the following information from this German invoice text:
            - vendor
            - date
            - amount
            - iban
            - line_items (list of objects with 'description', 'quantity', 'price')

            Return the output strictly as a JSON object matching this structure.
            If a field is not found, return null for it.

            Text:
            {full_text}
            """

        response = model.generate_content(prompt)
        # Basic parsing to handle markdown blocks if returned
        text = response.text
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]

        return json.loads(text.strip())

    except Exception as e:
        print(f"Error during extraction: {e}")
        return {}
