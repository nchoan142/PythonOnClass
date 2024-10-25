KW = int(input("Enter numbers of KW: "))

if KW <= 100:
    money = 450 * KW
    print(money)
elif KW <= 200:
    money = 600 * KW
    print(money)
elif KW <= 300:
    money = 750 * KW
    print(money)
elif KW <= 500:
    money = 900 * KW
    print(money)
elif KW <= 1000:
    money = 1000 * KW
    print(money)
elif KW > 1000:
    money = 1200 * KW
    print(money)