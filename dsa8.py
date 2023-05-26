def is_balanced(code):
    stack = []

    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if bracket_pairs[top] != char:
                return False

    return len(stack) == 0

# Example usage:
code_snippet = input("Enter a code snippet: ")

if is_balanced(code_snippet):
    print("All brackets are properly closed.")
else:
    print("Brackets are not properly closed.")
