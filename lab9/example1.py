# Harmonic Sum

def harmonic(x):
  if x == 1:
    return 1
  return 1/x + harmonic(x-1)

print(harmonic(5))