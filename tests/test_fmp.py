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