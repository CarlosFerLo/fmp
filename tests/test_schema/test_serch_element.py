import pytest
from fmp.schema import SearchElement

import pydantic

def test_fmp_search_element_is_a_pydantic_base_model () :
    assert issubclass(SearchElement, pydantic.BaseModel)
    
def test_fmp_search_element_has_properties_defined_in_the_docs () :
    """{
		"symbol": "PRAA",
		"name": "PRA Group, Inc.",
		"currency": "USD",
		"stockExchange": "NasdaqGS",
		"exchangeShortName": "NASDAQ"
	}
    """
    search_element = SearchElement(
        symbol="PRAA",
        name="PRA Group, Inc.",
        currency="USD",
        stockExchange="NasdaqGS",
        exchangeShortName="NASDAQ"
    )
    
    assert search_element.symbol == "PRAA"
    assert search_element.name == "PRA Group, Inc."
    assert search_element.currency == "USD"
    assert search_element.stockExchange == "NasdaqGS"
    assert search_element.exchangeShortName == "NASDAQ"
    
    