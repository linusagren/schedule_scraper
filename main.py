from parser import get_schedule
from webhook import send_message

def main():
    mode = "live" # live | mock

    schedule = get_schedule(mode)

    if not schedule:
        return

    # Status handling
    match schedule["status"]:
        case "complete":
            room, start, end = schedule["classroom"], schedule["start_time"], schedule["end_time"]
            message = f"Tomorrow's schedule:\nRoom: {room}\nStart: {start}\nEnd: {end}"
            send_message(message)
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