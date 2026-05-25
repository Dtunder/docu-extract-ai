import os
import sys

# Ensure src modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.extractor import extract_document
from src.exporter import to_json

def main():
    print("--- DocuExtract-AI Demo ---")

    # Enforce mock mode for demo
    os.environ["MOCK_LLM"] = "true"
    print("MOCK_LLM is set to true. Bypassing Gemini API.\n")

    # Simulating the extraction of text from PDF using our mock plain text invoice
    sample_file = os.path.join("data", "sample_invoice.txt")

    try:
        with open(sample_file, "r", encoding="utf-8") as f:
            pages = [f.read()]
        print(f"Loaded sample data from {sample_file}")
    except FileNotFoundError:
        print(f"Error: {sample_file} not found. Are you running from the repo root?")
        sys.exit(1)

    print("\nExtracting structured data as 'invoice'...")
    extracted_data = extract_document(pages, doc_type="invoice")

    if not extracted_data:
        print("Extraction failed (returned empty dictionary).")
        sys.exit(1)

    print("\nExtraction Successful! Result Summary:")
    print("---------------------------------------")
    json_output = to_json(extracted_data)
    print(json_output)
    print("---------------------------------------")
    print("Demo completed successfully.")

if __name__ == "__main__":
    main()
