n=int(input())
ans=sum(1 for i in input().split() if int(i)%2 )
print(min(ans,n-ans))