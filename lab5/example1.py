# Multiplication Table

"""
number = int(input("Number:\n"))
for i in range(1,11):
  print(number, "x",i ,"=" ,number*i)
"""

# Of evens

N = int(input("How many numbers ?\n"))
evens = 0
for i in range (N):
  x = int(input("Enter an integer:"))
  if x % 2 == 0:
    evens += 1

print(evens/N*100,"%")

