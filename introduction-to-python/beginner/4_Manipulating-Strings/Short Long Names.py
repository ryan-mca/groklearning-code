name = input("Enter your name: ")

if len(name) <= 3:
    print(f"Hi {name}, you have a short name.")
elif len(name) > 3 and len(name) <= 8:
    print(f"Hi {name}, nice to meet you.")
else:
    print(f"Hi {name}, you have a long name.")