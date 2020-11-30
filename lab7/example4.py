#Employees


dict_employee = {}

for i in range(5):
  employee = input("What is the name of the employee ?\n")
  employee = str(employee)
  salary = input("What is the salary of the employee ?\n")
  salary = int(salary)
  dict_employee[employee] = salary

sorted_salary = sorted(dict_employee.values())
print(sorted_salary)

print(dict_employee)