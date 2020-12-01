n=int(input())
a=input()
b=input()
count=0
for i in range(n):
    min_digit=min(int(a[i]),int(b[i]))
    max_digit=max(int(a[i]),int(b[i]))
    count=count+min((max_digit-min_digit),(min_digit+10-max_digit))

print(count)
    