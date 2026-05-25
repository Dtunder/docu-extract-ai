import json
import csv
import io

def to_json(data: dict) -> str:
    """Exports dictionary to a JSON string."""
    return json.dumps(data, indent=2, ensure_ascii=False)

def to_csv(data: dict) -> str:
    """Exports dictionary to a CSV string. Handles simple key-value and nested list of dicts."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Write headers
    headers = []
    row = []

    for key, value in data.items():
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            continue # skip complex line items for the main row
        elif isinstance(value, list):
            headers.append(key)
            row.append(", ".join(str(v) for v in value))
        else:
            headers.append(key)
            # Ensure German number format stays intact (e.g. 1.234,56 €)
            row.append(str(value) if value is not None else "")

    writer.writerow(headers)
    writer.writerow(row)

    # Check if there are line_items or similar complex nested structures
    for key, value in data.items():
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            writer.writerow([])
            writer.writerow([f"--- {key} ---"])
            if len(value) > 0:
                sub_headers = list(value[0].keys())
                writer.writerow(sub_headers)
                for item in value:
                    sub_row = [str(item.get(k, "")) for k in sub_headers]
                    writer.writerow(sub_row)

    return output.getvalue()
