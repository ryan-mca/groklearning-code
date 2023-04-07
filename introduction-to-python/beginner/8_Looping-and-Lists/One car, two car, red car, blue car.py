cars = input("Cars: ").split()

red = 0
blue = 0

for car in cars:
    if car == "red":
        red+=1
    elif car == "blue":
        blue+=1
    else: continue

print(f"red: {red}")
print(f"blue: {blue}")