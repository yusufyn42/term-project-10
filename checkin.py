import os
from datetime import datetime


def check_in_attendee(registrations: list, registration_id: str) -> dict:
    for reg in registrations:
        if reg.get("id") == registration_id:
            reg["checked_in"] = True
            reg["check_in_time"] = datetime.now().isoformat(timespec="seconds")
            return reg
    raise ValueError("Registration not found")


def list_checked_in_attendees(registrations: list, event_id: str) -> list:
    result = []
    for reg in registrations:
        if reg.get("event_id") == event_id and reg.get("checked_in"):
            result.append(reg)
    return result


def generate_badge(attendee: dict,
                   registration: dict,
                   directory: str) -> str:
    os.makedirs(directory, exist_ok=True)

    filename = f"{attendee.get('id', 'unknown')}_badge.txt"
    path = os.path.join(directory, filename)

    lines = [
        f"Name: {attendee.get('name', '')}",
        f"Ticket: {registration.get('ticket_type', '')}",
        f"Event ID: {registration.get('event_id', '')}",
        f"Registration ID: {registration.get('id', '')}",
    ]

    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return path


def session_attendance(registrations: list,
                       event_id: str,
                       session_id: str) -> dict:
    total = 0
    checked_in = 0

    for reg in registrations:
        if reg.get("event_id") != event_id:
            continue

        sessions = reg.get("sessions", [])
        if session_id in sessions:
            total += 1
            if reg.get("checked_in"):
                checked_in += 1

    return {
        "event_id": event_id,
        "session_id": session_id,
        "registered": total,
        "checked_in": checked_in,
    }
