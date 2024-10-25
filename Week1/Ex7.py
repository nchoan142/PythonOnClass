score = float(input("Enter score: "))

if score < 50:
    print("Xep loai Yeu")
elif score <= 59:
    print("Xep loai Trung binh")
elif score <= 69:
    print("Xep loai Trung binh Kha")
elif score <= 79:
    print("Xep loai Kha")
elif score <= 100:
    print("Xep loai Gioi")
else:
    print("Khong hop le")