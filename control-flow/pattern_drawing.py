pattern = int(input("Enter the size of the pattern: "))

sides = 0

while sides < pattern:
    for num in range(pattern):
        print("*", end="")
    print() #for a new line

    sides += 1