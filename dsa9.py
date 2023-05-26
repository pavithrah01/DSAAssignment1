def reverse_stack(stack):
    if not stack:
        return

    # Remove the top element from the original stack
    top = stack.pop()

    # Reverse the remaining stack using recursion
    reverse_stack(stack)

    # Insert the top element at the bottom of the reversed stack
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return

    # Remove the top element from the stack
    top = stack.pop()

    # Insert the item at the bottom of the stack using recursion
    insert_at_bottom(stack, item)

    # Put the top element back on top of the stack
    stack.append(top)

# Example usage:
stack = list(input("Enter the stack elements: "))

print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)
