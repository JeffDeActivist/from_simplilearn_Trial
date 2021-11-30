x = int(input("Enter number of rows"))
y = 2 * x - 1
n = y

while n >= 1:
    space = y - n // 2
    for j in range(1, space + 1):
        print(" ", end="")

    for i in range(1, n + 1):
        print("*", end="")
    n = n - 2
    print()
