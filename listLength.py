# length of a list
a = [1, 2, 3, "jeff"]
length = 0
i = 0
try:
    while a[i]:
        length += 1
        i += 1
except IndexError:
    print(length)
