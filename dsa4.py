def find_first_non_repeated_character(string):
    char_count = {}

    # Count the occurrence of each character
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeated character
    for char in string:
        if char_count[char] == 1:
            return char

    # Return None if no non-repeated character is found
    return None

# Get user input for the string
string = input("Enter a string: ")

result = find_first_non_repeated_character(string)
if result:
    print("The first non-repeated character is:", result)
else:
    print("No non-repeated character found in the string.")
