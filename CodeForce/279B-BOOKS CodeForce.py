
n,t=map(int,input().split())
a=list(map(int,input().split()))
s=0
max_count=0
count=0
discarded=0
for i in range(n):

    s=s+a[i]
    if (t < s):
        s=s-a[discarded]
        discarded+=1



print(n-discarded)
