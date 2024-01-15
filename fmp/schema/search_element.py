from pydantic import BaseModel

class SearchElement (BaseModel) :
    symbol: str
    name: str
    currency: str
    stockExchange: str
    exchangeShortName: str