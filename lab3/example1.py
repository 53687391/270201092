# Absolute Value

"""
number = float(input("What is the number? \n"))
if number < 0:
  number = number*-1
  print("Absolute value: ",number)
else:
  print("Absolute value: ",number)

"""

# Minimum Value

"""
number_1 = float(input("What is the number1 ?\n"))
number_2 = float(input("What is the number2 ?\n"))
number_3 = float(input("What is the number3 ?\n"))

print("Minimum value = ",min(number_1,number_2,number_3))

"""

# Graduation Condition

"""
gpa = float(input("What is your gpa ?\n"))
lecture_num = int(input("What is the number of lectures ?\n"))

if gpa < 2:
  if lecture_num < 47:
    print("Not enough nomber of lectures and GPA!")
  else:
    print("Not enough GPA!")
else:
  if lecture_num < 47:
    print("Not enough number of lectures")
  else:
    print("GRADUATED!!!")
"""

# Ticket Discount

"""
age = int(input("What is your age ?\n"))
price = 3
if age < 6 or age > 60:
  print("Free ticket.")
elif age >= 6 and age < 18:
  print("%50 ticket discount.",price/2,"$")
else:
  print("No discount",price,"$")
"""





  
