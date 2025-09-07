attendee_names = set()

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
attendee_name = input("Attendee name: ")

# TODO: Add attendee_name to attendee_names
for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")

# TODO: Remove your name from attendees (if there)
absent_count = int(input("How many attendees are absent? "))
for _ in range(absent_count): 
    absent_name = input("Enter absent attendee name: ")
    if absent_name in attendee_names:
        attendee_names.remove(absent_name)

print(attendee_names)