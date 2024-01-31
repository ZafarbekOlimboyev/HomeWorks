a=list(map(int,input().split()))
b=int(input())
print(b-sum(a) if b-sum(a) > 0 else 0)