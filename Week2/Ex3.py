def areaRectangle(length, width):
    return length * width

def square(x):
    return x * x

def factorial(x):
    while True:
        if x == 1:
            return 1
        else:
            return x * factorial(x-1)

print(factorial(4))