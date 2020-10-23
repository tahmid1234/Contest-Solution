for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int, input().split()))
    a.sort()
    max_amount=a[n-1]
    i=n-2
    for _ in range(k):
        max_amount=max_amount+a[i]
        i=i-1
    print(max_amount)