from sys import stdin
import operator
def read():
    return stdin.readline().strip()


n,m=map(int,read().split())
r=-1
if m%n==0:
 m//=n;r=0
 for d in 2,3:
  while m%d==0:m//=d;r+=1
print((r,-1)[m>1])
