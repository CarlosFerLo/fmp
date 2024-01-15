from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

from .utils import load_api_key

class FMP (BaseModel) :
    api_key: str = Field(default_factory=load_api_key, validate_default=True)