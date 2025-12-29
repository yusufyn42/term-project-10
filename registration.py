def _find_event(events: list, event_id: str) -> dict | None:

    for event in events:
        if event.get("id") == event_id:
            return event
    return None


def _count_confirmed(registrations: list, event_id: str) -> int:

    count = 0
    for reg in registrations:
        if reg.get("event_id") == event_id and reg.get("status") == "confirmed":
            count += 1
    return count


def create_registration(registrations: list,
                        registration_data: dict,
                        events: list) -> dict:

    event_id = registration_data["event_id"]
    event = _find_event(events, event_id)

    if event is None:
        raise ValueError("Event not found")


    reg_id = registration_data.get("id")
    if reg_id is None:
        reg_id = f"R{len(registrations) + 1}"

    confirmation_code = f"{event_id}-{reg_id}"

    confirmed_count = _count_confirmed(registrations, event_id)
    capacity = event.get("capacity", 0)

    if confirmed_count < capacity:
        status = "confirmed"
        seat_number = confirmed_count + 1
    else:
        status = "waitlisted"
        seat_number = None

    amount = registration_data.get("amount", event.get("price", 0.0))

    registration = {
        "id": reg_id,
        "event_id": event_id,
        "attendee_id": registration_data["attendee_id"],
        "ticket_type": registration_data.get("ticket_type", "General"),
        "status": status,
        "seat_number": seat_number,
        "payment_method": registration_data.get("payment_method", "cash"),
        "payment_status": "paid" if status == "confirmed" else "pending",
        "amount": amount,
        "confirmation_code": confirmation_code,
    }

    registrations.append(registration)
    return registration


def promote_waitlist(registrations: list, event_id: str) -> dict | None:


    for reg in registrations:
        if reg.get("event_id") == event_id and reg.get("status") == "waitlisted":
            confirmed_count = _count_confirmed(registrations, event_id)
            reg["status"] = "confirmed"
            reg["seat_number"] = confirmed_count + 1
            reg["payment_status"] = "paid"
            return reg

    return None


def cancel_registration(registrations: list,
                        registration_id: str,
                        events: list) -> dict:

    for reg in registrations:
        if reg.get("id") == registration_id:
            reg["status"] = "cancelled"
            reg["payment_status"] = "refunded"
            return reg

    raise ValueError("Registration not found")


def transfer_ticket(registrations: list,
                    registration_id: str,
                    new_attendee_id: str) -> dict:

    for reg in registrations:
        if reg.get("id") == registration_id:
            reg["attendee_id"] = new_attendee_id
            return reg

    raise ValueError("Registration not found")


def calculate_event_revenue(registrations: list,
                            event_id: str) -> float:
    
    total = 0.0
    for reg in registrations:
        if reg.get("event_id") == event_id and reg.get("status") == "confirmed":
            amount = reg.get("amount", 0.0)
            total += float(amount)
    return total
