import json


def load_events(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_events(path: str, events: list) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)


def create_event(events: list, event_data: dict) -> dict:
    # id yoksa E1, E2, ... ver
    if "id" not in event_data:
        event_data["id"] = f"E{len(events) + 1}"
    if "sessions" not in event_data:
        event_data["sessions"] = []
    events.append(event_data)
    return event_data


def update_event(events: list, event_id: str, updates: dict) -> dict:
    for event in events:
        if event.get("id") == event_id:
            event.update(updates)
            return event
    raise ValueError("Event not found")


def add_session(events: list, event_id: str, session_data: dict) -> dict:
    for event in events:
        if event.get("id") == event_id:
            if "id" not in session_data:
                session_data["id"] = f"S{len(event.get('sessions', [])) + 1}"
            event.setdefault("sessions", []).append(session_data)
            return session_data
    raise ValueError("Event not found")


def list_sessions(events: list, event_id: str) -> list:
    for event in events:
        if event.get("id") == event_id:
            return event.get("sessions", [])
    return []
