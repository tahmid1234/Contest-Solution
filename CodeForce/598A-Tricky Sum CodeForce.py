for _ in range(int(input())):
    n=int(input())
    total=int((n*(n+1))//2)
    sub=2
    total_sub=1
    while True:
        if(sub>n):
            break
        total_sub=total_sub+sub
        sub=sub*2
    
    print(total-(2*total_sub))
