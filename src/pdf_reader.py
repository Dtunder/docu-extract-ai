from PyPDF2 import PdfReader

def extract_text(file_path: str) -> list[str]:
    """Extracts text from a PDF file, returning a list of strings (one per page)."""
    try:
        reader = PdfReader(file_path)
        pages = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
            else:
                pages.append("")
        return pages
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return []
