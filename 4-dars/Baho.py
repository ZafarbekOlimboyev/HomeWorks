a=int(input())
if a>=38:
    if a%5>=3:
        while True:
          a += 1
          if a%5 == 0:
            print(a)
            break
    else:
        print(a)
else:
    print(a)