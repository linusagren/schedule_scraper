from bs4 import BeautifulSoup
import scraper

def parse_schedule(html):
    soup = BeautifulSoup(html, "html.parser")
    classroom = soup.find("div", class_="room")

    if classroom is not None:
        return classroom.get_text().strip()

    return None

if __name__ == '__main__':
    tomorrow = scraper.get_next_day()

    if tomorrow is not None:
        raw_html = scraper.get_schedule(tomorrow)

        if raw_html is not None:
            classroom = parse_schedule(raw_html)

            if classroom is not None:
                print(f"Classroom: {classroom}")
            else:
                print("No class in school tomorrow.")
        else:
            print("Could not retrieve schedule.")

    else:
        print("No weekday schedule to check.")