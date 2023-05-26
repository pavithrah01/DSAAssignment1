def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Example usage:
n = int(input("Enter the number of disks: "))

print("Tower of Hanoi steps:")
tower_of_hanoi(n, 'A', 'B', 'C')
