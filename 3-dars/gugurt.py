list_of_gugurt = {"0" : 6, "1" : 2, "235" : 5,"4" : 4, "6" : 6, "7" : 3, "8" : 7, "9" : 6}
def gugurt(x):
  s = 0
  for i in x:
    if i in "235":
      s += 5
    else:
      s += list_of_gugurt[i]
  return s

x = input()

print(gugurt(x))