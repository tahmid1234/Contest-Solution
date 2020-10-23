from collections import defaultdict
input()

dict=defaultdict(int)
rect=0
sqr=0
for item in input().split():

    dict[item]+=1
    if(dict[item]%4==0):

        sqr+=1
        rect-=1
    elif(dict[item]%4==2):
        rect+=1

for _ in range(int(input())):
    a,b=input().split()
    sqr-=dict[b]//4
    if dict[b]%4>1:
        rect-=1
    if(a=='+') :

        dict[b]+=1

    else:
            dict[b]-=1


    sqr+=dict[b]//4
    if(dict[b]%4>1):
        rect+=1

    if(sqr>1):
        print("YES")
    elif (sqr>0 and rect>1):
        print("YES")
    else:
        print("NO")
