import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

PAGE_ACCESS_TOKEN = os.getenv("PAGE_FB_TOKEN")
url = "https://graph.facebook.com/v21.0/me/messages"
RECIPIENT_IDS = ["6718498071598570"]
def send_message(recipient_id: str= "6718498071598570", message_text: str= "bot send"):
    payload = json.dumps({
    "message": "{\"text\":\"" + message_text + "\"}",
    "recipient": "{\"id\":" + recipient_id + "}"
    })
    headers = {
    'Authorization': f'Bearer {PAGE_ACCESS_TOKEN}',
    'Content-Type': 'application/json'
    }
    return requests.request("POST", url, headers=headers, data=payload)

send_message()

