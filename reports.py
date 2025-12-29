def attendance_report(events: list, registrations: list) -> dict:
    report: dict = {}

    for event in events:
        event_id = event.get("id")
        registered = 0
        checked_in = 0

        for reg in registrations:
            if reg.get("event_id") == event_id:
                registered += 1
                if reg.get("checked_in"):
                    checked_in += 1

        report[event_id] = {
            "registered": registered,
            "checked_in": checked_in,
        }

    return report


def revenue_report(events: list, registrations: list) -> dict:
    report: dict = {}

    for event in events:
        event_id = event.get("id")
        total = 0.0
        outstanding = 0.0

        for reg in registrations:
            if reg.get("event_id") != event_id:
                continue

            amount = float(reg.get("amount", 0.0))

            if reg.get("payment_status") == "paid":
                total += amount
            else:
                outstanding += amount

        report[event_id] = {
            "revenue": total,
            "outstanding": outstanding,
        }

    return report


def session_popularity(events: list, registrations: list) -> dict:
    result: dict = {}

    for event in events:
        event_id = event.get("id")
        sessions = event.get("sessions", [])
        event_info: dict = {}

        for session in sessions:
            session_id = session.get("id")
            count = 0

            for reg in registrations:
                if reg.get("event_id") != event_id:
                    continue
                if session_id in reg.get("sessions", []):
                    count += 1

            event_info[session_id] = count

        result[event_id] = event_info

    return result


def export_report(report: dict, filename: str) -> str:
    lines = []
    for key, value in report.items():
        lines.append(f"{key}: {value}")

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return filename
