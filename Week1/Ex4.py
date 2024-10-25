salary_per_hour = int(input("Enter salary per hour: "))
work_time = int(input("Enter work time: "))


if work_time > 40:
    total_money = (work_time - 40) * 1.5 * salary_per_hour + 40 * salary_per_hour
    print(total_money)
else: 
    total_money = salary_per_hour * work_time
    print(total_money)

tax = 0.1
money_before_tax = total_money
money_after_tax = total_money - (total_money * tax)
print("Total money before tax: ", money_before_tax)
print("Total money after tax: ", money_after_tax)