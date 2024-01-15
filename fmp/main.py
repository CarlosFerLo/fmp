from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

import requests

from .schema import SearchElement, GeneralSearchInput
from .utils import load_api_key

class FMP (BaseModel) :
    api_key: str = Field(default_factory=load_api_key, validate_default=True)
    
    def general_search (self, general_search_input: GeneralSearchInput) -> List[SearchElement] :
        response = requests.get(
            url="https://financialmodelingprep.com/api/v3/search",
            params={
                "query": general_search_input.query,
                "limit": general_search_input.limit,
                "exchange": general_search_input.exchange,
                "apikey": self.api_key
            }
        )
        
        response.raise_for_status()
        
        return [SearchElement(**search_element) for search_element in response.json()]