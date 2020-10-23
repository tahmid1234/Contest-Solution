import  math
for _ in range(int(input())):
    n,k=map(int,input().split())
    unique=0
    prev_element=-1
    for element in map(int,input().split()):
        if(element!=prev_element):
            unique+=1
            prev_element=element
    if(k>=unique):
        print(1)
    elif(k==1):
        print(-1)
    else:

        print(1+math.ceil((unique-k)/(k-1)))