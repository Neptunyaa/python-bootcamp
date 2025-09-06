# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
# "yellow"  -> print "Wait..."
# "red"     -> print "Stop"

match color_input :
    case "green" | "Green": 
        print("go")
    case "yellow" | "Yellow":
        print("wait...")
    case "red" | "Red":
        print("stop")
    case _:
        print("i dont know")    