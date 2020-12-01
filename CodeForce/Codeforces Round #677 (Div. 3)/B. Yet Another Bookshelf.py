for _ in range(int(input())):
    n=input()
    a=list(map(int,input().split()))
    count=0
    zeros=0
    ones=0
    for item in a:
        if(item==1):
            ones=ones+1
            count=zeros
        elif(item==0 and ones>0):
            zeros=zeros+1
    print(count)