count=0

for _ in range(int(input())):

    n=int(input())
    a=list(map(int,input().split()))
    dict={}
    prev=a[0]
    dict[prev]=0

    for i in range(1,n):
        item=a[i]

        if (prev != item):
            if prev in dict:



                dict[prev]=dict[prev]+1
            else:
                dict[prev]=2
            prev=item

    if a[n-1] not in dict:
        dict[a[n-1]]=1
    val=dict[a[0]]
    for key,value in dict.items():

        val=min(value,val)

    print(val)
