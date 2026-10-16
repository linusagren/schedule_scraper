from bs4 import BeautifulSoup
import scraper

def parse_schedule(html):
    soup = BeautifulSoup(html, "html.parser")
    classroom = soup.find("div", class_="room")

    if classroom is not None:
        return classroom.get_text().strip()

    return None

def get_classroom():
    tomorrow = scraper.get_next_day()

    if tomorrow is None:
        print("No weekday schedule to check")
        return

    raw_html = scraper.get_schedule(tomorrow)

    if raw_html is None:
        print("Could not retrieve schedule.")
        return

    classroom = parse_schedule(raw_html)

    if classroom is None:
        print("No class in school tomorrow.")
        return

    return classroom

if __name__ == '__main__':
    print(get_classroom())