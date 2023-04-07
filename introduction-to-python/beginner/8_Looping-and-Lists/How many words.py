words = []

word = input("Word: ")

while word != "":
    if word not in words:
        words.append(word)
    word = input("Word: ")

print(f"You know {len(words)} unique word(s)!")