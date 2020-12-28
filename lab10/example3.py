#Sum of a list

def sum_of_list(x):
  if not isinstance(x,list):
    return x
  else:
    summ = 0
    for a in x:
      summ += sum_of_list(a)
    return summ



a_list = [3,12,76,[4,56,43],[2,8],81,75]
print(sum_of_list(a_list))