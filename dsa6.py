def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)

    return stack.pop()

# Example usage:
postfix_expression = input("Enter a postfix expression: ")

prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)
