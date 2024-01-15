import pytest
from fmp.schema import GeneralSearchInput

import pydantic

def test_fmp_general_search_input_is_a_pydantic_base_model () :
    issubclass(GeneralSearchInput, pydantic.BaseModel)
    
def test_fmp_general_search_input_has_query_string_and_otpional_limit_int_exchange_string () :
    gsi = GeneralSearchInput(
        query="AA",
        limit=10,
        exchange="NYSE"
    )
    
    assert gsi.query == "AA"
    assert gsi.limit == 10
    assert gsi.exchange == "NYSE"
    
    gsi = GeneralSearchInput(
        query="BB"
    )
    
    assert gsi.query == "BB"
    assert gsi.limit is None
    assert gsi.exchange is None
