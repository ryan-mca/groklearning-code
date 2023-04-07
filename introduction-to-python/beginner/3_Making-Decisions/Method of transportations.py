weather = input("Is it currently raining? ")

if weather == "Yes":
    print("You should take the bus.")
else:
    distance = int(input("How far in km do you need to travel? "))
    if distance < 2:
        print("You should walk.")
    elif distance >=2 and distance <= 10:
        print("You should ride your bike.")
    else:
        print("You should take the bus.")