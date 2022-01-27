from numpy import char


given_word: str = input("Type in a word: ")

char_looking_for: str = input("Type a single character you would like to search for in the word you provided: ")

i: int = 0

while i<len(given_word) :
    if given_word[i] ==  char_looking_for:
        print(char_looking_for + " occurs at index " + str(i))
    i = i + 1
