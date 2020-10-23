for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    index_list=[]
    for i in range(n):
        for j in range(i+1,n):

            if(a[i]!=a[j]):
                index_list.append(str(i+1)+" "+str(j+1))
            else:
                break
    if(len(index_list)==0):
        print("NO")
    else:
        print("YES")
        for item in index_list:
            print(item)
