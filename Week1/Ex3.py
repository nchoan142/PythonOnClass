import math

width = int(input("Enter width: "))
length = int(input("Enter length: "))

rec_perimeter = (width + length) * 2
rec_square = width * length
print(rec_square)
print(rec_perimeter)

side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

tri_perimeter = side1 + side2 + side3
half_perimeter = tri_perimeter / 2
tri_square = math.sqrt(half_perimeter*(half_perimeter - side1)*(half_perimeter - side2)*(half_perimeter - side3))
print(tri_perimeter)
print(tri_square)

radius = int(input("Enter radius: "))
cirle_perimeter = 2 * 3.14 * radius
cirle_square = pow(radius) * 3.14
print(cirle_perimeter)
print(cirle_square)

side = int(input("Enter side: "))
square_perimeter = side * 4
square_square = side * side
print(square_perimeter)
print(square_square)