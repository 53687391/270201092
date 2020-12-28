#Basic Multiplication

def multipli_3(n):
  if n == 1:
    return 3 
  else:
    return 3 + multipli_3(n-1)

print(multipli_3(6))