from math import sqrt

def koshi(x, y):
  a = sqrt(x * y)
  b = (x + y) / 2
  print(a,b)
  if b > a:
    return ">"
  elif a > b:
    return "<"
  else:
    return"="

x, y = map(int, input().split())

print(koshi(x,y))