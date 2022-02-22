"""Making a computer based wordle."""

__author__ = "730468950"
# from numpy import False_
# import secrets
# from unittest.util import strclass


def contains_char(searched_word: str, checking_char: str) -> bool:
    """Checks to see if a letter is contained in a string."""
    assert len(checking_char) == 1
    i: int = 0
    # This loop loops throuhg a word to see if it contains a given character
    while i < len(searched_word):
        if searched_word[i] == checking_char:
            return True
        i += 1
    return False 


def emojified(guess: str, secret: str) -> str:
    """Takes guess and turns it into its color coded meaning."""
    assert len(guess) == len(secret)
    j: int = 0
    # secret_word = "python"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    output: str = ""
    # loop will go though lenght of guess and assign each character in the guess its poper color box
    while j < len(guess):
        if secret[j] == guess[j]:
            output += GREEN_BOX
        elif contains_char(secret, guess[j]) is True:
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        j += 1
    return output


def input_guess(expected_length: int) -> str:
    """Makes sure the user input is the correct length."""
    guess = input(f"Enter a {expected_length} character word: ")
    # this loop goes until the user inputs a guess of the correct length 
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = False
    secret: str = "codes"

    # This loop prompts each turn until the player wins or runs out of turns
    while turn < 7 and won is False:
        print(f"=== Turn {turn}/6 ===")
        current_guess: str = input_guess(len(secret))
        print(emojified(current_guess, secret))
        if current_guess == secret:
            won = True
        else:
            turn += 1
    if won is True:
        print(f"You won in {turn}/6 turns!")
    elif won is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
    