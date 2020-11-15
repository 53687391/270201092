# Sum of the last two digits
"""
x = int(input("Enter the value: \n"))

if x < 10:
  total = x
else:
  ones = x % 10
  tens = (x//10) % 10
  total = ones + tens

print("Sum of the last 2 digits:", total)
"""

# Leap Year
"""
year = int(input("Enter the year:\n"))

if year % 100 == 0:
  if year % 400 != 0:
    print (year,"is not a leap year")
  else:
    print(year, "is a leap year")
elif year % 4 == 0:
  print (year, "is a leap year")
else:
  print (year ,"is not a leap year")
  """

# Sum of list
"""
nums = [8,60,43,55,25,134,1]
sum_of_list = 0
for i in range(len(nums)):
  sum_of_list += nums[i]

print("Sum of the list is",sum_of_list,".")

"""

# Power
"""
a = int(input("What is a:\n"))
b = int(input("What is  b:\n"))
result = 1

if b >= 0:
  for i in range(b):
    result = result*a
else:
  for i in range(0,b,-1):
    result = result/a

print(result)
"""

# Factorial

n = int(input("What is the number you want to calculate its factorial?\n"))
result = 1
for i in range(1,n+1):
  result = result * i
print(result)
