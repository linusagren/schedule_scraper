from bs4 import BeautifulSoup
import scraper

def parse_schedule(html: str):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("span", class_="name")
    classroom = soup.find("span", class_="room")
    time = soup.find("span", class_="time")
    search_result = soup.find("div", class_="meta")

    if not all([classroom, time]):
        if search_result is not None and "Inga bokningar matchade din sökning under perioden." in search_result.get_text():
            print("No search results found.")
            return {"status": "no_results"}

        return {"status": "incomplete"}

    class_name, title = title.get_text().strip().split("- ", 1)
    classroom = classroom.get_text().strip()
    start_time, end_time = time.get_text().strip().split("–", 1)

    class_schedule = {
        "class_name": class_name,
        "title": title,
        "classroom": classroom,
        "start_time": start_time,
        "end_time": end_time,
        "status": "complete"
        }
    
    return class_schedule

def get_schedule(mode: str = "live"):
    if mode not in ["live", "mock"]:
        raise ValueError(f"'{mode}' is not a valid mode.")
    if mode == "mock":
        raw_html = scraper.get_mock_schedule()

        if raw_html is None:
            return {"status": "fetch_failure"}
        
        return parse_schedule(raw_html)

    tomorrow = scraper.get_next_day()

    if tomorrow is None:
        return {"status": "weekend"}

    raw_html = scraper.get_raw_schedule(tomorrow)

    if raw_html is None:
        return {"status": "fetch_failure"}

    schedule = parse_schedule(raw_html)

    return schedule

if __name__ == '__main__':
    print(get_schedule())