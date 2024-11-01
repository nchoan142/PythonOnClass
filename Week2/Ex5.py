num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

def compare(num1, num2, num3):
    if num1 > num2:
        if num2 > num3:
            return num1

    if num1 > num3:
        if num3 > num2:
            return num1

    if num2 > num1:
        if num1 > num3:
            return num2
    
    if num2 > num3:
        if num3 > num1:
            return num2

    if num3 > num1:
        if num1 > num2:
            return num3

    if num3 > num2:
        if num2 > num1:
            return num3

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

def average(num1, num2, num3, num4):
    return (num1 + num2 + num3 + num4) / 4