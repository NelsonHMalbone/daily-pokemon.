import smtplib, ssl, certifi
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

def send_email(message): # this is a string
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USERNAME")
    password = os.getenv("APPPASS")
    recipients = os.getenv("RECIPIENTS")

    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = recipients
    msg["Subject"] = "Daily News"
    msg.set_content(message)

    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)

