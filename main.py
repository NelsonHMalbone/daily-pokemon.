import requests
from dotenv import load_dotenv
import os
from pathlib import Path

# loading dotenv file.
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path) #reads .env file

API_KEY = os.getenv("MYAPIKEY")

# hard stop if api is missing
if not API_KEY:
    raise RuntimeError("API_KEY not set")

user_input = input("Enter topic to get news: ")
url = f'https://newsapi.org/v2/everything?q={user_input}&from=2025-12-17&sortBy=publishedAt&apiKey={API_KEY}'


req = requests.get(url)
content = req.json()

for index, article in enumerate(content['articles'], start=1):
    print(f'{index}: {article['title']}')


