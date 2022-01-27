"""Making a one attemp wordle."""

__author__ = "730468950"

# from numpy import char

secret_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# getting the users certain number letter guess
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

index1: int = 0
response: str = ""
character_found: bool = False

# going through the guess to determine the correspondong color boxes
while index1 < len(guess):
    if guess[index1] == secret_word[index1]:
        response = response + GREEN_BOX
    else:
        character_found = False
        searching_index2: int = 0
        # determining between if a box should be yellow or white
        while searching_index2 < len(guess):
            if guess[index1] == secret_word[searching_index2]:
                character_found = True
            searching_index2 = searching_index2 + 1
        if character_found is True:
            response = response + YELLOW_BOX
        else:
            response = response + WHITE_BOX
    index1 = index1 + 1

print(response)

# printing if the guess was correct or not
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
