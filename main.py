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
user_input_date = input("Enter date to get news ex 2025-12-20: ")
url = f'https://newsapi.org/v2/everything?q={user_input}&from={user_input_date}&sortBy=publishedAt&apiKey={API_KEY}'


req = requests.get(url)
content = req.json()

for index, article in enumerate(content['articles'], start=1):
    print(f'{index}: {article['title']} \n '
          f'{article["description"]} \n '
          f'{article["url"]} \n')


