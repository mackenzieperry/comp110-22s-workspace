"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730468950"

number_of_instances: int = 0
full_word = input("Enter a 5-character word: ")

if len(full_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_char = input("Enter a single character: ")

if len(single_char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_char + " in " + full_word)

if full_word[0] == single_char:
    print(single_char + " found at index 0")
    number_of_instances = number_of_instances + 1
if full_word[1] == single_char:
    print(single_char + " found at index 1")
    number_of_instances = number_of_instances + 1
if full_word[2] == single_char:
    print(single_char + " found at index 2")
    number_of_instances = number_of_instances + 1
if full_word[3] == single_char:
    print(single_char + " found at index 3")
    number_of_instances = number_of_instances + 1
if full_word[4] == single_char:
    print(single_char + " found at index 4")
    number_of_instances = number_of_instances + 1
if number_of_instances == 0:
    print("No instances of " + single_char + " found in " + full_word)
else:
    if number_of_instances == 1:
        print("1 instance of " + single_char + " found in " + full_word)
    if number_of_instances > 1:
        print(str(number_of_instances) + " instances of " + single_char + " found in " + full_word)
