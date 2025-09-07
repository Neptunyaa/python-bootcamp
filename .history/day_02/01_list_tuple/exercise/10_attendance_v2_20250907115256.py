attendee_names = ["Alice", "Bob", "Charlie"]

attendee_count = int(input("Attendee count: "))
absent_count = int(input("How many attendees are absent? "))

# TODO: For every attendee expected:
for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")
    # TODO: Add attendee_name to attendee_names
    attendee_names.append(attendee_name)

# TODO: Remove absent attendees (if they’re there)
for _ in range(absent_count):
    absent_name = input("Enter absent attendee name: ")
    if absent_name in attendee_names:
        attendee_names.remove(absent_name)

print(attendee_names)
