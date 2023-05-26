def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage:
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

reverse_array(arr)
print("Reversed array:", arr)

# with user input
def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Get user input for the array
array_input = input("Enter the integers in the array (space-separated): ")
arr = list(map(int, array_input.split()))

print("Original array:", arr)

reverse_array(arr)
print("Reversed array:", arr)
