current = int(input("Current floor: "))
dest = int(input("Destination floor: ")) + 1

for i in range(current, dest):
    print(f"Level {i}")