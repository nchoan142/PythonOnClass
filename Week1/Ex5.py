salary = int(input("Enter salary: "))
allowance = int(input("Enter allowance: ")) #phụ cấp
salary_advance = int(input("Enter salary advance: ")) #tạm ứng
insurance = salary * 0.05 #bảo hiểm

real_salary = salary + allowance - salary_advance - insurance
print(real_salary)