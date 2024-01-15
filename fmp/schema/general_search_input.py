from pydantic import BaseModel, Field
from typing import Optional

class GeneralSearchInput (BaseModel) :
    query: str
    limit: Optional[int] = Field(default=None, ge=1)
    exchange: Optional[str] = Field(default=None)
    
    