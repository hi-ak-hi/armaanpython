started=False
command=""#empty string
while True:
    command=input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - quit
        """)
    elif command == "start":
        if started:
            print("the car is already started")
        else:
            started=True
            print("car started...") 
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started=True
            print("the car stopped")
    elif command == "quit":
        break
    else:
        print("sorry, i dont understnd your request")
print("done")