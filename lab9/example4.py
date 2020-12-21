# Simple Time

import time

def countdown(x):
  if x == 0:
    print("DANGER DANGER !!!")
    return None
  
  print("You have",x,"seconds remain")
  time.sleep(1)
  return countdown(x-1)

countdown(5)