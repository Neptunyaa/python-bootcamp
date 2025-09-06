# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
# "yellow"  -> print "Wait..."
# "red"     -> print "Stop"
# Everything else   -> print "Malfunction"

if color_input == "green":
    print("go")
elif color_input == "yellow":
    print("wait...")
elif color_input == "red":
    print("stop")
else:
    print("I dont know")        