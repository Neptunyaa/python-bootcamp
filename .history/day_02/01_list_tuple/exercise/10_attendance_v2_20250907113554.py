attendee_names = []

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")
# TODO: Add attendee_name to attendee_names
    attendee_names.append(attendee_name)
# TODO: Remove your name in attendees (if it’s there)
    if attendee_absent in attendee_names:
        attendee_absent = input("Enter absent attendee name: ")
        attendee_names.remove(attendee_absent)
print(attendee_names)
