numberuno = int(input("enter your first number: "))
numbertwo = int(input("enter you second number: "))

if numberuno/numbertwo == 1:
        print("It appears that you have entered 2 of the same numbers")
if numberuno > 100 or numbertwo > 100:
        print("one of your numbers are over the limit of 100")
if numberuno < 1 or numbertwo < 1:
        print("one of your numbers are below the range")

commonfactors1 = []


THECOMMONFACTORS = []


def factors():
    for i in range(1, numberuno + 1):
        if(numberuno % i == 0 and numbertwo % i == 0):
            commonfactors1.append(i)
factors()
for i in commonfactors1:
    if i == i in commonfactors1:
        THECOMMONFACTORS.append(i)
    if i != i in commonfactors1:
        print("no gcf")


sus = max(THECOMMONFACTORS)
print(f"Your greatest common factors is: {sus}")





