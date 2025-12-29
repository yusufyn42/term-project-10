import json


def load_attendees(path: str) -> list:

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_attendees(path: str, attendees: list) -> None:

    with open(path, "w", encoding="utf-8") as file:
        json.dump(attendees, file, indent=4)


def _generate_attendee_id(attendees: list) -> str:

    number = len(attendees) + 1
    return f"A{number}"


def register_attendee(attendees: list, profile: dict) -> dict:

    if "id" not in profile:
        profile["id"] = _generate_attendee_id(attendees)

    attendees.append(profile)
    return profile


def authenticate_attendee(attendees: list, email: str, pin: str) -> dict | None:

    for attendee in attendees:
        if attendee.get("email") == email and attendee.get("pin") == pin:
            return attendee
    return None


def update_attendee(attendees: list, attendee_id: str, updates: dict) -> dict:

    for attendee in attendees:
        if attendee.get("id") == attendee_id:
            attendee.update(updates)
            return attendee

   
    raise ValueError("Attendee not found")
