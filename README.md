# docu-extract-ai
AI-powered PDF document extractor. Upload invoice or contract → get structured JSON/CSV. DATEV-compatible fields.

## Setup
1. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Set `GEMINI_API_KEY` in `.env` file (or use `MOCK_LLM=true` for testing).
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Features
- Extracts vendor, date, amount, IBAN, and line items from invoices.
- Extracts parties, date, value, and terms from contracts.
- Handles German number formats (e.g., `1.234,56 €`).
- Export to JSON or CSV.
