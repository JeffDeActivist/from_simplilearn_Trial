"""continue and break """
# break
x = "hey there.How are you today."
for i in x:
    if i == ".":
        break
    print(i, end="")


# continue
for j in [1, 2, 3, 4, 5, 3, 8, 9, 10, 11]:
    if j == 3:
        continue
    print(j)
