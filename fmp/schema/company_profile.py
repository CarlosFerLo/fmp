from pydantic import BaseModel, field_validator
from typing import Tuple

class CompanyProfile (BaseModel) :
    symbol: str
    price: float
    beta: float
    volAvg: float
    mktCap: float
    lastDiv: float
    range: Tuple[float, float]
    changes: float
    companyName: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchange: str
    exchangeShortName: str
    industry: str
    website: str
    description: str
    ceo: str
    sector: str
    country: str
    fullTimeEmployees: int
    phone: str
    address: str
    city: str
    state: str
    zip: str
    dcfDiff: float
    dcf: float
    image: str
    ipoDate: str
    defaultImage: bool
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool
    
    @field_validator("range", mode="before")
    def make_range_a_tuple (cls, v) :
        if isinstance(v, tuple) :
            return v
        s = v.split("-")
        if len(s) != 2 :
            raise ValueError("range must be a string with two numbers separated by a dash")
        return (float(s[0]), float(s[1]))