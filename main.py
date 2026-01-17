import requests
from dotenv import load_dotenv
import os
from pathlib import Path



# loading dotenv file.
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path) #reads .env file

API_KEY = os.getenv("MYAPIKEY")
print(API_KEY)


if not API_KEY:
    raise RuntimeError("API_KEY not set")

url = f'https://newsapi.org/v2/everything?q=tesla&from=2025-12-17&sortBy=publishedAt&apiKey={API_KEY}'

print(url)



