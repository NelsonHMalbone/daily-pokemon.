import requests
from dotenv import load_dotenv
import os
from pathlib import Path
from send_email import send_email

# loading dotenv file.
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path) #reads .env file

API_KEY = os.getenv("MYAPIKEY")

# hard stop if api is missing
if not API_KEY:
    raise RuntimeError("API_KEY not set")

#user_input = input("Enter topic to get news: ")
#user_input_date = input("Enter date to get news ex 2025-12-20: ")
url = (f'https://newsapi.org/v2/everything?'
       f'q=Code&'
       f'sortBy=publishedAt'
       f'&apiKey={API_KEY}&'
       f'language=en')


req = requests.get(url)
content = req.json()

body = ""
for article in content['articles'][:10]:
    body = body + article['title'] + '\n' + article['description'] + 2*"\n"
print("email was sent")

send_email(body)
