#Pascal's Triangle

def pascals_triangle_last_line(n):
  if n == 1:
    return [1]

  else:

    line = [1]
    previous_line = pascals_triangle_last_line(n-1)
    for i in range(len(previous_line)-1):
      line.append(previous_line[i] + previous_line[i+1])
    line += [1]

    return line

def pascals_triangle(n):
  if n == 1:
    return print([1])
  else:
    print(pascals_triangle_last_line(n))
    return pascals_triangle(n-1)

pascals_triangle(5)