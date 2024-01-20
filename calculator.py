def addition():
    print("Addition")
    num = float(input("Enter the number: "))
    total = 0
    ans = 0
    while num != 0:
        ans = ans + num
        total += 1
        num = float(input("Enter another number (0 to calculate): "))
    return [ans,total]

def subtraction ():
    print("Subtraction")
    num = float(input("Enter the number: "))
    total = 0
    ans = 0
    while num != 0:
        ans = ans - num
        total += 1
        num = float(input("Enter another number (0 to calculate): "))
    return [ans,total]

def multiplication ():
    print("Multiplication")
    num = float(input("Enter the number: "))
    total = 0
    ans = 1
    while num != 0:
        ans = ans * num
        total+=1
        num = float(input("Enter another number (0 to calculate): "))
    return [ans,total]

def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

while True:
    list = []
    print(" My first python program!")
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter 'a' for addition")
    print(" Enter 's' for subtraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")

    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invalid character")
    else:
        break