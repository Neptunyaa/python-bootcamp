attendee_names = ["Alice", "Bob", "Charlie"]

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
for _ in range(attendee_count):
	attendee_name = input("Attendee name: ")
	# TODO: Add attendee_name to attendee_names
	attendee_names.append(attendee_name)

print(attendee_names)
