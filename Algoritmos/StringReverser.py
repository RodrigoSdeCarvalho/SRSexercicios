def reverse_string(string_to_reverse:str) -> str:
    reversed_string = ""
    for i in range(len(string_to_reverse)):
        reversed_string += string_to_reverse[len(string_to_reverse) - i - 1]

    return reversed_string


print(reverse_string("programação"))
