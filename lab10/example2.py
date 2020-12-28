#Hailstone

def hailstone(x):
  x = int(x)
  if x == 1:
    return print(x)
  elif x % 2 == 0:
    print(x)
    return hailstone(x/2)
  else:
    print(x)
    return hailstone(3*x+1)

hailstone(11)