for _ in range(int(input())):
    x=int(input())-1
    count_type=0
    n=1

    while(x>=0):
        count_type+=1
        n=2*n+1
        total_cells=(n*(n+1))//2
        x=x-total_cells

    print(count_type)