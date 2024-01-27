def uchburchak(x : list):
    while True:
        x = list(x)
        x.sort()
        x.reverse()
        for i in x:
            index = x.index(i)
            for y in x[index + 1:]:
                for z in x[index + 2:]:
                    if i + y > z and i + z > y and y + z > i:
                        a = [i,y,z]
                        a.sort()
                        return f"{a[0]} {a[1]} {a[2]}"
        else:
            return -1
a = input()
x = list(map(int, input().split()))
print(uchburchak(x))