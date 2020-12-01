
a={1,2}
b={2,3}

c=[]
c.append(a)
c.append(b.copy())
print(c)
b.clear()
b.add(4)
print(c)
'''
from sys import stdin
import math
def read():
    return stdin.readline().strip()

a=[]
n,k,t=map(int,read().split())
box=(n*t)/100
floorBox=math.floor(box)
extraBox=(box-floorBox)*k

for _ in range(floorBox):
    a.append(k)
if(floorBox!=n):
    a.append(math.floor(extraBox))
for _ in range(n-floorBox-1):
    a.append(0)

'''