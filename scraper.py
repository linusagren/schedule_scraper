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


def get_schedule(date_tomorrow: str):
    """
    Attempts to fetch the schedule for class AIU26 from the Campus website.
    """
    try:
        r = requests.get(f'https://campusvarbergtv.se/schemasok/?startDateTime={date_tomorrow}&endDateTime={date_tomorrow}&text=AIU26&showAll=1&showAll=1', timeout=10)
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