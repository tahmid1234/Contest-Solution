
from sys import stdin
def read():
    return stdin.readline().strip()

dict={}
output=[]

iteration=int(read())

max_val=-1

for _ in range(iteration):
    item=read()
    
    if dict.get(item) is None:
        dict[item]=0 
    dict[item]+=1 
    max_val = max(dict[item],max_val)
#max_val=max(dict.values())
for k,v in dict.items():
    
    if(max_val==v):
        output.append(k)
    
    
output.sort()
print('\n'.join(output))
