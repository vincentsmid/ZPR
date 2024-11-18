def jesoudelny(num1, num2):
  if num2 == 0 and num1 > 1:
    return True
  elif num2 == 0 and num1 == 1:
    return False
  return jesoudelny(num2, num1 % num2)


def tabulka(k):
  if k > 99 or k < 1:
    print("ERROR")
    return
  buffer = 0
  for i in range(1, k+1):
    for j in range(1, k+1):
      if jesoudelny(i, j):
        print("x", end="")
      else:
        print(" ", end="")
      buffer += 1
      if j != k:
        print("|", end="")
        buffer += 1
    print()
    if i != k:
      for z in range(buffer):
        print("-", end="")
      print()
    buffer = 0