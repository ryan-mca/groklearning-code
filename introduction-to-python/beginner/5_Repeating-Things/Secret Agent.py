text = input("Message? ")
text2 = ""

for i in range(len(text) - 1):
    if i % 3 == 0:
        text2 = text2 + text[i] + " "

print(text2.strip())