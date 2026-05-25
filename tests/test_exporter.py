import json
from src.exporter import to_json, to_csv

def test_to_json():
    data = {"vendor": "Muster GmbH", "amount": "1.234,56 €"}
    json_str = to_json(data)
    loaded = json.loads(json_str)
    assert loaded["vendor"] == "Muster GmbH"
    assert loaded["amount"] == "1.234,56 €"

def test_to_csv_flat():
    data = {"vendor": "Muster GmbH", "amount": "1.234,56 €"}
    csv_str = to_csv(data)
    # Checks if German number format is preserved
    assert "1.234,56 €" in csv_str
    assert "vendor;amount" in csv_str.replace('\r', '')

def test_to_csv_with_line_items():
    data = {
        "vendor": "Muster GmbH",
        "amount": "1.234,56 €",
        "line_items": [
            {"desc": "Item 1", "price": "100,00 €"}
        ]
    }
    csv_str = to_csv(data)
    # Check if nested content causes correct headers to be written
    assert "--- line_items ---" in csv_str
    assert "desc;price" in csv_str.replace('\r', '')
    assert "Item 1;100,00 €" in csv_str.replace('\r', '')

def test_to_csv_with_list_of_strings():
    data = {
        "parties": ["Party A", "Party B"],
        "date": "01.01.2024"
    }
    csv_str = to_csv(data)
    assert "parties;date" in csv_str.replace('\r', '')
    assert "Party A, Party B" in csv_str
