import os
from dotenv import load_dotenv

def load_api_key () -> str :
    load_dotenv()
    try : 
        api_key = os.environ["FMP_API_KEY"]
    except KeyError :
        raise ValueError("Must either pass the 'api_key' parameter or set the 'FMP_API_KEY' env variable.")
    
    return api_key