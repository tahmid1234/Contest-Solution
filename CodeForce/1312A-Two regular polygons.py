from sys import stdin
def read():
    return stdin.readline().strip()


t=int(read())
for _ in range (t):
    a,b=(map(int,read().split()))
    print(("NO","YES")[a%b==0])