def find_pairs(arr, target):
    pairs = []
    num_dict = {}

    for num in arr:
        complement = target - num
        if complement in num_dict:
            pairs.append((complement, num))
        num_dict[num] = True

    return pairs

arr = [2, 4, 6, 3, 1, 7, 5, 9]
target_sum = 10

result = find_pairs(arr, target_sum)
print(result)


# with input from user
def find_pairs(arr, target):
    pairs = []
    num_dict = {}

    for num in arr:
        complement = target - num
        if complement in num_dict:
            pairs.append((complement, num))
        num_dict[num] = True

    return pairs

# Get user input for the array
array_input = input("Enter the integers in the array (space-separated): ")
arr = list(map(int, array_input.split()))

# Get user input for the target sum
target_sum = int(input("Enter the target sum: "))

result = find_pairs(arr, target_sum)
print("Pairs with the given sum:")
for pair in result:
    print(pair)
