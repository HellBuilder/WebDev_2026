a = int(input())
b = []

b = [int(num) for num in input().split()]

for i in range(0,a,2):
    print(b[i], end=' ')