import pytest
import fmp

import os
import pydantic

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["FMP_API_KEY"]

def test_FMP_object_is_a_pydantic_base_model () :
    assert issubclass(fmp.FMP, pydantic.BaseModel)
    
def test_FMP_object_can_be_initialized_by_passing_an_api_key () :
    router = fmp.FMP(api_key=api_key)
    
    assert router.api_key == api_key
    
def test_FMP_object_loads_api_key_from_environ_if_no_api_key_provided () :
    router = fmp.FMP()
    
    assert router.api_key == api_key
    
def test_FMP_object_has_general_search_method () :
    router = fmp.FMP(api_key=api_key)
    
    assert hasattr(router, "general_search")
    
def test_FMP_object_general_search_method_accepts_general_search_input_object_and_returns_list_of_search_elements () :
    router = fmp.FMP(api_key=api_key)
    
    gsi = fmp.schema.GeneralSearchInput(
        query="AA",
        limit=10,
        exchange="NYSE"
    )
    
    search_elements = router.general_search(gsi)
    
    assert isinstance(search_elements, list)
    
    for search_element in search_elements :
        assert isinstance(search_element, fmp.schema.SearchElement)
        