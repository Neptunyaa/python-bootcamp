total = 10
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        number = int(input("Enter number: "))
        result = total + number
        print(result)
    if command == "sub": 
        number = int(input("Enter number: "))
        result = total - number
        print(result)
    elif command == "exit":
        running = False
