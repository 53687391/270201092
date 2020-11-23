# Multiplication Table

"""
number = int(input("Number:\n"))
for i in range(1,11):
  print(number, "x",i ,"=" ,number*i)
"""

# Of evens

"""
N = int(input("How many numbers ?\n"))
evens = 0
for i in range (N):
  x = int(input("Enter an integer:"))
  if x % 2 == 0:
    evens += 1

print(evens/N*100,"%")
"""

# Matching Digits

"""
number1 = int(input("First number ?\n"))
number2 = int(input("Second number ?\n"))
minn = min(number1,number2)
minn = str(minn)
match = 0
for i in range(len(minn)):
  if number1 % 10**i == number2 % 10**i:
    match += 1
print("There are",match,"digit(s) matched.")

"""

# Password Checker

password = "abc123"
passw_help = password[0]
while True:
  passw = input("Enter the password:\n")
  if passw == password:
    print("Welcome")
    break
  elif passw == "help":
    print("a")
  else:
    print("Wrong Password")


