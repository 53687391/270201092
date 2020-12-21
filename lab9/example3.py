# Get Number of Evens

def get_evens(l):
  return _get_evens_recursive(l,0)

def _get_evens_recursive(l,c =0):
  if len(l) == 0:
    return c
  
  current = l.pop()
  if current >= 0 and current %2 == 0:
    c += 1
  
  return _get_evens_recursive(1,c)


print(get_evens([0, 1, 2, 3, 4, 5, 6]))
