import json
import os
import requests
from dotenv import load_dotenv

def send_message(content: dict):

    if load_dotenv():
        print("Environment loaded successfully.")

    KEY = os.getenv("DISCORD_WEBHOOK_URL")

    if not KEY: # safeguard if KEY is None or empty
        print("ERR: Could not find webhook URL")
        return
    
    try:
        data = {"payload_json": json.dumps(content)}

        with open("icons/lesson.png", "rb") as f:
            files = {"files[0]": ("lesson.png", f)}
            params = {"with_components": "true"}
            r = requests.post(KEY, data=data, files=files, timeout=10, params=params)

        r.raise_for_status()

        if r.status_code == 204:
            print("Message sent to Discord successfully.")
    except requests.exceptions.Timeout as err:
        print(err)
    except requests.HTTPError as err:
        print(err)
    except requests.RequestException as err:
        print(err)