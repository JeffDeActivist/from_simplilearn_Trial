# for loops
for i in [1, 2, 3, 4, 5, 6]:
    if i == 6:
        print(i)

# while loops with break
a = 1
while a > 0:
    if a == 7:
        break

    print(a)
    a += 1
print(a)

# for loop with break
for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    if j == 7 or j == 10:
        continue
    print(j)
