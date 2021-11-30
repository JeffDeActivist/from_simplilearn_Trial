"""a simple code to test if one knows the multiples of 7"""
# stops if you enter a multiple of 7
a = 1
# while will run until the condition a % 7 != 0 is satisfied
while a % 7 == 0:
    a = int(input("enter a multiple of 7"))
    if a % 7 == 0:
        print(a, "is a multiple of 7")
    else:
        print(a, "is not multiple of 7", )
