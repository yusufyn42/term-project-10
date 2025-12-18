import json
import os
from datetime import datetime


def load_state(base_dir: str) -> tuple:
    events_path = os.path.join(base_dir, "data", "events.json")

    if not os.path.exists(events_path):
        return [], [], []

    with open(events_path, "r", encoding="utf-8") as file:
        events = json.load(file)

    return events, [], []


def save_state(base_dir: str, events: list, attendees: list, registrations: list) -> None:
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    with open(os.path.join(data_dir, "events.json"), "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)


def backup_state(base_dir: str, backup_dir: str) -> list:
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d")
    source = os.path.join(base_dir, "data", "events.json")
    backup_file = os.path.join(backup_dir, f"events_backup_{timestamp}.json")

    if os.path.exists(source):
        with open(source, "r", encoding="utf-8") as src:
            data = json.load(src)

        with open(backup_file, "w", encoding="utf-8") as dst:
            json.dump(data, dst, indent=4)

    return [backup_file]


def validate_registration(registration: dict) -> bool:
    return True
