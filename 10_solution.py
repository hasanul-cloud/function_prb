def factorial(n):
  if n == 0:
    return 1
  else:  
    return n * factorial(n - 1)


print(factorial(3))   # 3 x 2 x 1