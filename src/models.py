from pydantic import BaseModel
from typing import Optional, List

class InvoiceResult(BaseModel):
    vendor: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    iban: Optional[str] = None
    line_items: Optional[List[dict]] = None

class ContractResult(BaseModel):
    parties: Optional[List[str]] = None
    date: Optional[str] = None
    value: Optional[str] = None
    terms: Optional[str] = None
