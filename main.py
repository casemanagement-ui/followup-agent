import argparse


def generate_24hr_message(client_name: str, practice_name: str, booking_link: str) -> str:
    return (
        f"Hi {client_name}, this is a gentle check-in from {practice_name}. "
        "We know the first day after reaching out can feel like a lot, and we want you to know "
        "there is space for you whenever you are ready. "
        f"If it feels helpful, you can choose a time here: {booking_link}."
    )


def generate_1week_message(client_name: str, practice_name: str, booking_link: str) -> str:
    return (
        f"Hi {client_name}, just checking in from {practice_name}. "
        "If this week has been full, that is completely understandable. "
        "Support is still available, and we are happy to meet you where you are. "
        f"If you would like to schedule, here is the link: {booking_link}."
    )


def generate_3week_message(client_name: str, practice_name: str, booking_link: str) -> str:
    return (
        f"Hi {client_name}, this is a warm follow-up from {practice_name}. "
        "No need to respond unless you want to—we simply wanted to leave the door open for care. "
        "Whenever it feels right, we would be glad to support you. "
        f"You can book at any time here: {booking_link}."
    )


def build_message(client_name: str, practice_name: str, booking_link: str, stage: str) -> str:
    generators = {
        "24hr": generate_24hr_message,
        "1week": generate_1week_message,
        "3week": generate_3week_message,
    }
    return generators[stage](client_name, practice_name, booking_link)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate staged follow-up messages for a therapy practice."
    )
    parser.add_argument("--client-name", required=True)
    parser.add_argument("--practice-name", required=True)
    parser.add_argument("--booking-link", required=True)
    parser.add_argument("--stage", required=True, choices=["24hr", "1week", "3week"])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    message = build_message(
        client_name=args.client_name,
        practice_name=args.practice_name,
        booking_link=args.booking_link,
        stage=args.stage,
    )
    print(message)


if __name__ == "__main__":
    main()
