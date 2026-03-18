a = int(input())

for i in range(a):
    for j in range(a):
        if(i + j < a - 1):
            print(0, end=' ')
        elif(i + j == a - 1):
            print(1, end=' ')
        elif(i + j > a - 1):
            print(2, end=' ')
    print()
