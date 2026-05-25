import os
from src.extractor import extract_document
from src.models import InvoiceResult, ContractResult

def test_mock_llm_invoice_extraction(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "true")
    pages = ["dummy text"]
    result = extract_document(pages, "invoice")

    # Verify using pydantic models to ensure validation
    validated_result = InvoiceResult(**result)
    assert validated_result.vendor == "Muster GmbH"
    assert validated_result.date == "15.05.2024"
    assert validated_result.amount == "1.234,56 €"
    assert validated_result.iban == "DE12345678901234567890"
    assert len(validated_result.line_items) == 2
    assert validated_result.line_items[0]["price"] == "1.000,00 €"

def test_mock_llm_contract_extraction(monkeypatch):
    monkeypatch.setenv("MOCK_LLM", "true")
    pages = ["dummy text"]
    result = extract_document(pages, "contract")

    validated_result = ContractResult(**result)
    assert validated_result.parties == ["Muster GmbH", "Tech Solutions AG"]
    assert validated_result.date == "01.10.2023"
    assert validated_result.value == "50.000,00 €"
    assert validated_result.terms == "Netto 30 Tage"

def test_extraction_missing_fields_pydantic():
    # Model allows Optional fields
    result = {"vendor": "Test Vendor"}
    validated = InvoiceResult(**result)
    assert validated.vendor == "Test Vendor"
    assert validated.amount is None
    assert validated.line_items is None
