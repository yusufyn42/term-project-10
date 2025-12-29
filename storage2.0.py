import json
import os
from datetime import datetime


def load_state(base_dir: str) -> tuple[list, list, list]:
    data_dir = os.path.join(base_dir, "data")
    events_path = os.path.join(data_dir, "events.json")
    attendees_path = os.path.join(data_dir, "attendees.json")
    registrations_path = os.path.join(data_dir, "registrations.json")

    def _load(path: str) -> list:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    events = _load(events_path)
    attendees = _load(attendees_path)
    registrations = _load(registrations_path)

    return events, attendees, registrations


def save_state(base_dir: str,
               events: list,
               attendees: list,
               registrations: list) -> None:
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    with open(os.path.join(data_dir, "events.json"), "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    with open(os.path.join(data_dir, "attendees.json"), "w", encoding="utf-8") as file:
        json.dump(attendees, file, indent=4)

    with open(os.path.join(data_dir, "registrations.json"), "w", encoding="utf-8") as file:
        json.dump(registrations, file, indent=4)


def backup_state(base_dir: str, backup_dir: str) -> list[str]:
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d")
    source = os.path.join(base_dir, "data", "events.json")
    backup_file = os.path.join(backup_dir, f"events_backup_{timestamp}.json")

    if os.path.exists(source):
        with open(source, "r", encoding="utf-8") as src:
            data = json.load(src)
        with open(backup_file, "w", encoding="utf-8") as dst:
            json.dump(data, dst, indent=4)

    return [backup_file]


def validate_registration(registration: dict) -> bool:
    if "event_id" not in registration:
        return False
    if "attendee_id" not in registration:
        return False
    return True
