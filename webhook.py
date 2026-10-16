import requests
import os
from dotenv import load_dotenv

payload = {"content": "Message test, classroom variables go here later..."}

if load_dotenv():
    print("Environment loaded successfully.")

    KEY = os.getenv("DISCORD_WEBHOOK_URL")

    if not KEY: # safeguard if KEY is None or empty
        print("ERR: Could not find webhook URL")
    else:
        try:
            r = requests.post(KEY, json=payload, timeout=10)
            r.raise_for_status()

            if r.status_code == 204:
                print("Message sent to Discord successfully.")
        except requests.exceptions.Timeout as err:
            print(err)
        except requests.HTTPError as err:
            print(err)
        except requests.RequestException as err:
            print(err)