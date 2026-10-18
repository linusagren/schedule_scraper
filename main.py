from parser import get_schedule
from webhook import send_message
from embed import create_embed

def main():
    mode = "mock" # live | mock

    schedule = get_schedule(mode)

    if not schedule:
        return

    # Status handling
    match schedule["status"]:
        case "complete":
            embed_schedule = create_embed(schedule)
            send_message(embed_schedule)
        case "incomplete":
            print("Could not retrieve full schedule.")
        case "no_results":
            print("Search returned no results.")
        case "weekend":
            print("No class on weekends.")
        case "fetch_failure":
            print("Could not fetch schedule.")
        case _:
            raise ValueError(f"Unknown status: {schedule['status']}")

if __name__ == "__main__":
    main()