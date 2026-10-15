from bs4 import BeautifulSoup
from scraper import get_schedule

def parse_schedule(html):
    soup = BeautifulSoup(html, "html.parser")
    classroom = soup.find("div", class_="room")

    if classroom is not None:
        return classroom.get_text().strip()

    return None

if __name__ == '__main__':
    raw_html = get_schedule()

    if raw_html is not None:
        soup = parse_schedule(raw_html)
        