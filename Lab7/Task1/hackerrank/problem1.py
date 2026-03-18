n = int(input())
integer_list = map(int, input().split())

a = tuple()

for i in range(n):
    a += (integer_list[i],)

print(hash(a))