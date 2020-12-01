import math
for _ in range(int(input())):
    n=int(input())
    root=math.ceil((-1+math.sqrt(1+8*n))/2)
    ans=root*(root+1)//2
    if(ans-n==0):
        print(root)
    elif(ans-n==1):
        print(root+1)
    else:
        print(root)


