from parser import get_classroom
from webhook import send_message

def main():
    classroom = get_classroom()

    if not classroom:
        return

    send_message(f"Tomorrow's classroom: {classroom}")

if __name__ == "__main__":
    main()