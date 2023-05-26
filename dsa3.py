def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated = str1 + str1

    if str2 in concatenated:
        return True
    else:
        return False

# Example usage:
string1 = "hello"
string2 = "llohe"

result = are_rotations(string1, string2)
if result:
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")


#with user input
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated = str1 + str1

    if str2 in concatenated:
        return True
    else:
        return False

# Get user input for the strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = are_rotations(string1, string2)
if result:
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")
