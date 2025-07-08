from pydantic import BaseModel
from typing import Optional

class EmailDraftRequest(BaseModel):
    to: str
    from_: str  # 'from' is a reserved keyword
    title: str
    body: Optional[str] = ""
