for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    answer="NO"
    for i in range(n-1):
        if(a[i]<=a[i+1]):
            answer="YES"
            break;
    print(answer)