input()
maxVal=0
ans=0
for ele in list(map(int,input().split())):
    
    ans=maxVal+ele
    maxVal+=max(0,ele)
    print(ans)
    