"""Tuples and lists"""
# Lists
b = [1, 2, 3, 4, "jeff", "python", 2, 4, 6]
print(b)
b.append("kevin")
print(b)

print(b[5:7])
print(b.reverse())

# Tuples
t = (1, 1, 2, 3, "Python", "Sql")
print(t.count(1))
s = (4, "OPP")
# tuple s is being concatenated to tuple t
t = t + s
print(t)
cT = tuple(range(5))
print(cT)
# list b is being converted into a tuple
cb = tuple(b)
print(cb)
