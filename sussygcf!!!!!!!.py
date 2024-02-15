numberuno = int(input("enter your first number: "))
numbertwo = int(input("enter you second number: "))


if numberuno/numbertwo == 1:
        print("It appears that you have entered 2 of the same numbers")

if numberuno > 100 or numbertwo > 100:
        print("one of your numbers are over the limit of 100")

if numberuno < 1 or numbertwo < 1:
        print("one of your numbers are below the range")

def factors1():
    for i in range(1, numberuno + 1):
        if(numberuno % i == 0):
            print(i)


def factors2():
    for i in range(1, numbertwo + 1):
        if(numbertwo % i == 0):
            print(i)

factors1()
factors2()