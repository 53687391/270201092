def bin_to_dec(n):
  s = 0
  n_rev = str(n)[::-1]
  for i in range(len(n)):
    s + = (int(n_rev[i]) * (2**i))
  return s

print(bin_to_dec(10010))

def dec_to_bin(d):
  b = ""
  while d > 0:
    b += str(d%2)
    d = d // 2
  return (b[::-1])

def main():
  b = "10010"
  print(binary_to_dec)
  d = 18
  print(dec_to_binary(d))

main()
