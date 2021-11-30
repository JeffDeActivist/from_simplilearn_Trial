"""lists tuples and sets recap"""
a = [1, 2, 3, 4, 5, 5, 3, 4, 3, 2]
print("initial list a is", a)
a.append("python")
print("list of a after first append", a)
# changing sequence type
c = set(a)
print("set c", c)
d = tuple(a)
print("tuple d", d)
c.add("SQL")
print("c after add", c)
a[6] = "O.B.B"
print("a after altering of index 6", a)
a.remove(5)
print("a after removing 5", a)
a.remove(5)
print("a after removing 5", a)
# get index of an item in a list
print("index of 1 in list a is", a.index(1))
# iterating over a list
for i in a:
    print(a[3])
"""Dictionaries"""
progLang = {1: "python",
            2: "sql",
            3: "css",
            4: "Django",
            5: "data science",
            6: "java script"
            }
print("this is my first dictionary", progLang)
# access dict value
try:
    print(progLang[7])
except KeyError:
    print(progLang)

from collections import defaultdict

progLang = defaultdict(lambda: "Java")
print(progLang[7])

"""isinstance"""
b = 1
while b <= 20:
    if isinstance(b, int):
        print(b)
        b += 1
"""Lists"""
# removing duplicates
list1 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 4, 5]
set1 = set(list1)
list2 = list(set1)
print("this is list 1", list1)
print("this is set 1", set1)
print("this is list2", list2)
list3 = list(set(list1))
print("this is list 3", list3)
# # test for membership
if 1 in set1:
    print("True")
