"""Some fucntions of dictionaries."""

__author__ = "730468950"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary and makes all the values the new keys and keys the new values."""
    inverted_dict: dict[str, str] = {}
    for key in dictionary:
        new_key: str = dictionary[key]
        if new_key in inverted_dict:
            raise KeyError("The dictionary you are trying to invert would have mulitple keys.")
        else:
            inverted_dict[new_key] = key
    return inverted_dict
# do I need to do something to address errors?


def favorite_color(dictionary: dict[str, str]) -> str:
    """Finds the mode color in a dict of peoples favorite colors."""
    favorite_color_counter: dict[str, int] = dict()
    # Setting up a dictionary with all of the colors in the sent dictionary
    # and giving them all counts of 0 that we will later add to
    for key in dictionary:
        print("dictionary[key]: " + dictionary[key])
        favorite_color_counter[dictionary[key]] = 0
    # adding 1 to the value of the dictionary favorite_color_counter each that color appears as a key
    for key in dictionary:
        favorite_color_counter[dictionary[key]] += 1
        count_of_that_color: int = favorite_color_counter[dictionary[key]]
        print("Adding 1 to " + dictionary[key])
        print(dictionary[key] + " count is " + str(count_of_that_color))
    max_number: int = 0
    favorite_color: str = ""
    # loops through favorite_color_counter and finds the max value
    for key in favorite_color_counter:
        if favorite_color_counter[key] > max_number:
            max_number = favorite_color_counter[key]
            favorite_color = key
    print("The mode color is " + favorite_color + " it occurs " + str(max_number) + " times")
    return favorite_color


def count(sent_list: list[str]) -> dict[str, int]:
    """Counts the number of times each element in a list is repeated."""
    return_dict: dict[str, int] = dict()
    for item in sent_list:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    print(return_dict)
    return return_dict


# def main() -> None:
#     # favorite_colors({"ellie": "Blue", "howie": "Green", "howard": "Red", "Joel": "Red", "Hidie": "Yellow"})
#     count([])
#     count(['1', '1', '2', '3', '2', '4', '2'])


# if __name__ == "__main__":
#     main()