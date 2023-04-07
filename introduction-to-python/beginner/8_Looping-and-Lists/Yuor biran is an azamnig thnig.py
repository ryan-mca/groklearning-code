word1, word2 = input("Enter words: ").split()

word1 = list(word1)
word2 = list(word2)

if word1[0] == word2[0] and word1[-1] == word2[-1]:
    word1.sort()
    word2.sort()
    if word1 == word2:
        print("Super Anagram!")
    else:
        print("Huh?")
else:
    print("Huh?")