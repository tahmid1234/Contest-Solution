for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    dict = {}
    b = []

    for i in a:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    index = -1
    
    for key, value in sorted(dict.items()):
        if (value == 1):

            index=a.index(key)+1
            break

    print(index)


