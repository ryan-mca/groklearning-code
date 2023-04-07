print("What is my favourite food?")

while True:
    guess = input("Guess? ")

    if guess != "electricity":
        print("Not even close.")
    else:
        break

print("You guessed it! Buzzzz")