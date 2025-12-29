from storage import load_state, save_state
from events import create_event
from attendees import register_attendee
from registration import create_registration


def main():
    base_dir = "."
    events, attendees, registrations = load_state(base_dir)

    print("Simple demo")

    if not events:
        event = {
            "name": "Sample Event",
            "location": "Istanbul",
            "start_date": "2025-01-01",
            "end_date": "2025-01-02",
            "capacity": 2,
            "price": 100.0,
            "description": "Demo",
        }
        create_event(events, event)

    if not attendees:
        attendee = {
            "name": "Test User",
            "email": "test@example.com",
            "pin": "1234",
            "ticket_type": "General",
        }
        register_attendee(attendees, attendee)

    if not registrations:
        reg_data = {
            "event_id": events[0]["id"],
            "attendee_id": attendees[0]["id"],
        }
        create_registration(registrations, reg_data, events)

    save_state(base_dir, events, attendees, registrations)
    print("Done")


if __name__ == "__main__":
    main()
