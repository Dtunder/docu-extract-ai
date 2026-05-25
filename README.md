# docu-extract-ai
AI-powered PDF document extractor. Upload invoice or contract → get structured JSON/CSV. DATEV-compatible fields.

This project allows German KMUs to upload their PDFs and extract relevant information (like vendor, date, amount, IBAN, line items) into structured data compatible with their tools.

## Setup
1. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables. Copy `.env.example` to `.env` and fill in your keys:
   - `GEMINI_API_KEY`: Your Google Gemini API Key.
   - `MOCK_LLM`: Set to `true` to bypass the LLM entirely and use mock data for testing (defaults to `false`).

## Running the App
Run the Streamlit app:
```bash
streamlit run app.py
```

## Running Tests
Run the test suite with pytest:
```bash
python -m pytest tests/
```

## Features
- Extracts vendor, date, amount, IBAN, and line items from invoices.
- Extracts parties, date, value, and terms from contracts.
- Handles German number formats (e.g., `1.234,56 €`).
- Export to JSON or CSV.
