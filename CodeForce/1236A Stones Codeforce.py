
for _ in range(int(input())):
    first_case,second_case=0,0
    a,b,c=map(int,input().split())
    min_b=min(b,c//2)
    first_case=min_b+min_b*2

    b=b-min_b

    min_b=min(a,b//2)
    first_case=first_case+min_b*2+min_b
    print(first_case)


