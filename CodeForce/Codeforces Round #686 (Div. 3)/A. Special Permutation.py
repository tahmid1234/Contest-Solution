for _ in range (int(input())):
    n=int(input())
    a=[n]
    for i in range (1,n,1):
       a.append(i)
    print(*a)

