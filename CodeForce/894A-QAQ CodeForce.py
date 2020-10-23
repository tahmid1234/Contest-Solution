s=input()
qCount=0
aCount=0
count=[]
for i in range(len(s)):
    if(s[i]=='Q'):
        qCount+=1
    if(qCount>0 and s[i]=='A'):
        count.append(qCount)
        
        aCount+=1
    

count=[i*(qCount-i) for i in count]


print(sum(count))