# Reverse list

def reverse_list(l):
  if len(l)== 0:
    return []
  
  return[l.pop()] + reverse_list(l)

print(reverse_list([1, 2, 3, 4]))