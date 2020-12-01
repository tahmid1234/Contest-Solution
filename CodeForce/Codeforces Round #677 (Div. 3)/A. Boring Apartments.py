count_match={1:1,2:3,3:6,4:10}

for _ in range(int(input())):
    number=input();
    pressedNumber=(int(number[0])-1)*10+count_match[len(number)]
    print(pressedNumber)
