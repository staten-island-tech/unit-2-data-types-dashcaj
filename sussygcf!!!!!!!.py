numberuno = int(input("enter your first number: "))
numbertwo = int(input("enter you second number: "))

if numberuno/numbertwo == 1:
        print("It appears that you have entered 2 of the same numbers")
if numberuno > 100 or numbertwo > 100:
        print("one of your numbers are over the limit of 100")
if numberuno < 1 or numbertwo < 1:
        print("one of your numbers are below the range")

commonfactors1 = []
commonfactors2 = []

THECOMMONFACTORS = []


def factors1():
    for i in range(1, numberuno + 1):
        if(numberuno % i == 0):
            commonfactors1.append(i)

def factors2():
    for i in range(1, numbertwo + 1):
        if(numbertwo % i == 0):
            commonfactors2.append(i)
factors1()
factors2()

for i in commonfactors1 and commonfactors2:
    if i == i in commonfactors1 and commonfactors2:
        THECOMMONFACTORS.append(i)
    if i != i in commonfactors1 and commonfactors2:
        print("no gcf")

    

sus = max(THECOMMONFACTORS)
print(f"Your greatest common factors is: {sus}")





