class MinStack:
    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, value):
        if value < self.min_value:
            # Update the minimum value
            self.min_value = value
        self.stack.append((value, self.min_value))

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()[0]

    def get_min(self):
        if not self.stack:
            return None
        return self.stack[-1][1]

# Example usage:
stack = MinStack()

# Push elements onto the stack
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(1)
stack.push(4)

# Get the smallest number
smallest_number = stack.get_min()
print("Smallest number:", smallest_number)
