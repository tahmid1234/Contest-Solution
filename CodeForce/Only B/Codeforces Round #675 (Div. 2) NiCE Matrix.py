
for _ in range(int(input())):
    n,m=map(int,input().split())
    array=[]

    for i in range(n):

        col = list(map(int, input().split()))
        array.append(col)
    count=0
    for row in range (n//2):
        for col in range(m//2):
            temp=[array[row][col],array[row][m-1-col],array[n-1-row][col],array[n-1-row][m-1-col] ]
            temp.sort()
            count+=(temp[3]+temp[2]-temp[0]-temp[1])


    if(n%2!=0):
        for col in range(m // 2):
            count+=abs(array[n//2][col]-array[n//2][m-1-col])
    if(m%2!=0):
        for row in range(n // 2):
            count+=abs(array[row][m//2]-array[n-1-row][m//2])


    print(count)

