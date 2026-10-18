import requests
import datetime as dt

def get_next_day():
    """
    Returns tomorrow's date as a string if it's a weekday.
    """
    today = dt.datetime.now()
    
    tomorrow = today + dt.timedelta(days=1)

    if tomorrow.isoweekday() <= 5:
        tomorrow = tomorrow.strftime("%Y-%m-%d")
        return tomorrow
    else:
        return None

def get_mock_schedule():
    """
    Attempts to fetch the schedule for class AIU26 from a html file.
    """
    try:
        with open("sample.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as err:
        print(err)

def get_raw_schedule(date_tomorrow: str):
    """
    Attempts to fetch the schedule for class AIU26 from the Campus website.
    """
    class_ = "AIU26"

    params = {
        "startDateTime": date_tomorrow,
        "endDateTime": date_tomorrow,
        "text": class_,
        "showAll": 1
        }

    try:
        r = requests.get('https://campusvarbergtv.se/schemasok/', params=params, timeout=10)
        r.raise_for_status()

        if r.status_code == 200:
            return r.text
        
    except requests.exceptions.Timeout as err:
        print(err)
    except requests.HTTPError as err:
        print(err)
    except requests.RequestException as err:
        print(err)
    
    return None