a, b = 0, 1
for _ in range(100):
  a, b = b, a + b
  print(format(a, 'b').replace('0', '○').replace('1', '●'))
