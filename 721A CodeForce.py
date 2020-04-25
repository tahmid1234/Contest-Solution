from sys import stdin
def read():
    return stdin.readline().strip()
read()
a=[len(i) for i in read().split('W') if i]
   

print(len(a), *a)