#Pascal's Triangle Last Line

"""
def pascals_triangle_last_line(n):
  if n == 1:
    return [1]

  else:

    line = [1]
    previous_line = pascals_triangle_last_line(n-1)
    line.append(previous_line[i] + previous_line[i+1])
    line += [1]

    return line

print(pascals_triangle_line(6))
"""