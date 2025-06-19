# function to print Ascii values of string input

def print_ascii_of_string(string):

    for character in string:

        ascii_value = ord(character)

        print(f"{character}-> {ascii_value}")


# invocation code

print_ascii_of_string('abc')

print_ascii_of_string('123')

print_ascii_of_string('ABC')