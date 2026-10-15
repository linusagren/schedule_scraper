import requests

def get_schedule():
    try:
        r = requests.get('https://campusvarbergtv.se/schemasok/?startDateTime=2026-10-20&endDateTime=2026-10-20&text=AIU26&showAll=1&showAll=1', timeout=10)
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

if __name__ == '__main__':
    data_raw = get_schedule()