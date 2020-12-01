n,m=map(int,input().split())

min_val=float("inf")
for _ in range(n):
    a,b=map(int,input().split())
    min_val=min(min_val,(a/b))
print(min_val*m)
