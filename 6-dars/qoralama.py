import math
import time

def tub(x):
    for i in range(2,int(math.sqrt(x) + 1)):
        if x % i == 0:
            return 0
    return 1

def tub_num(n):
    for i in range(3,n,2):
        if tub(i) == 1:
            yield i
if __name__ == "__main__":
    n = int(input("n : "))
    start_time = time.time_ns() // 1_000_000
    if n >=2:
        print(len(list(tub_num(n))) + 1)
    else:
        print(len(list(tub_num(n))))
    end_time = time.time_ns() // 1_000_000
    print((end_time - start_time), "millisecund")

# 10 000 000 -> tub sonlar 664579 ta    time -> 74 485 millisecund
# 1 000 000 -> tub sonlar 78498 ta time -> 3728 millisecund
# 10 000 -> tub sonlar 1229 ta  time -> 8 millisecund
