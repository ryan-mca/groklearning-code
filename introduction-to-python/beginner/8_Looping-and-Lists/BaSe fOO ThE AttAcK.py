code = input("code: ").split()

code.reverse()

says = ""

for word in code:
    if word[0].isupper():
        says += f"{word.lower()} "

print(f"says: {says.strip()}")