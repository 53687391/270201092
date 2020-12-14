
def is_prime(p):
  if p <= 1:
    return False
  for x in range (2,p):
    if p % x == 0:
      return False
  return True


def print_primes_between(a,b):
  for j in range(a,b):
    if is_prime(j) == True:
      print(j)


x = int(input("First integer :"))
y = int(input("Second integer :"))

print_primes_between(x,y)