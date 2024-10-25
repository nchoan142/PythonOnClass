print("1. Tinh dien tich hinh vuong")
print("2. Tinh dien tich hinh chu nhat")
print("3. Tinh dien tich hinh tam giac")
print("4. Tinh dien tich hinh thang")
print("5. Tinh dien tich hinh tron")
print("6. Thoat")

choice = int(input("Moi ban chon chuc nang: "))

if choice == 1:
    side = int(input("Nhap canh cua hinh vuong: "))
    square = side * side
    print(square)
elif choice == 2:
    length = int(input("Nhap chieu dai: "))
    width = int(input("Nhap chieu rong: "))
    square = length * width
    print(square)
elif choice == 6:
    return

while True:
    print("1. Tinh dien tich hinh vuong")
    print("2. Tinh dien tich hinh chu nhat")
    print("3. Tinh dien tich hinh tam giac")
    print("4. Tinh dien tich hinh thang")
    print("5. Tinh dien tich hinh tron")
    print("6. Thoat")

    choice = int(input("Moi ban chon chuc nang: "))

    if choice == 1:
        side = int(input("Nhap canh cua hinh vuong: "))
        square = side * side
        print(square)
    elif choice == 2:
        length = int(input("Nhap chieu dai: "))
        width = int(input("Nhap chieu rong: "))
        square = length * width
        print(square)
    elif choice == 6:
        break