import random
def get_rand_list(b,e,N):
  random_list = []
  for i in range(N):
    n = random.randint(b,e)
    random_list.append(n)
  return(random_list)


def get_overlap(x,y):
  intersection = []
  for i in range(len(x)):
    if x[i] in y:
      intersection.append(x[i])
  return intersection

x = get_rand_list(3,20,6)
y = get_rand_list(3,20,6)
print("First random list ->",x)
print("Second random list ->",y)
print("Overlap -->",get_overlap(x,y))