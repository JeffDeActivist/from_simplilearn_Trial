a = 3


def while_loop():
    global a
    while 3 <= a < 20:
        print("This is number:", a)
        a += 1


while_loop()

# inserting user_given values into a list
b = []
element = input("Enter elements to add into the list")
while element != '0' and len(b) < 5:
    b.append(element)
    element = input("Enter elements to add into the list")
