BERTHS = ["SU", "LB", "MB", "UB", "LB", "MB", "UB", "SL"]


def parse_pnr(pnr):
    """Split a 10 digit PNR into (zone digit, remaining number).

    Returns None if the PNR is not a string of exactly 10 digits.
    """
    if not isinstance(pnr, str):
        return None
    if len(pnr) != 10 or not pnr.isascii() or not pnr.isdigit():
        return None
    return int(pnr[0]), int(pnr[1:])


def journey_distance(distances_csv):
    """Return last station distance minus first from a CSV string.

    Returns None for non-string input, empty or non-numeric entries.
    """
    if not isinstance(distances_csv, str):
        return None
    try:
        distances = [int(d.strip()) for d in distances_csv.split(',')]
    except ValueError:
        return None
    return distances[-1] - distances[0]


def berth_type(seat):
    """Return (coach, berth) for a seat like 'S3-45'.

    Returns None if the seat is not in the form COACH-NUMBER.
    """
    if not isinstance(seat, str):
        return None
    parts = seat.split('-')
    if len(parts) != 2:
        return None
    coach, number = parts[0].strip(), parts[1].strip()
    if not coach:
        return None
    try:
        return coach.upper(), BERTHS[int(number) % 8]
    except ValueError:
        return None


def main():
    print("==== Running parse_pnr ====")
    user_input = input("Enter a 10 digit PNR (e.g. 4521367890): ")
    result = parse_pnr(user_input)
    print("Zone and Number:", result)

    print("\n==== Running journey_distance ====")
    user_input = input("Enter station distances as CSV (e.g. 0,120,340): ")
    result = journey_distance(user_input)
    print("Total Distance:", result)

    print("\n==== Running berth_type ====")
    user_input = input("Enter coach and seat (e.g. S3-45): ")
    result = berth_type(user_input)
    print("Coach and Berth:", result)


if __name__ == "__main__":
    main()