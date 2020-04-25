from sys import stdin
def read():
    return stdin.readline().strip()
a=[int(x) if 9-int(x)>int(x) else 9-int(x) for x in str(read())  ]
if a[0]==0:a[0]=9
print(*a, sep = '')
