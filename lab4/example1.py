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

#Leap Year


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