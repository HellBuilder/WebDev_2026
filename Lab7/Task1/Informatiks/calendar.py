a = int(input())
b = True
c = 0
a = a % 365
if(a > 59):
    a -= 59
    c = 3
    while(a > 29):
        if(b):
            a -= 31
            b = False
            c += 1
        else:
            a -= 30
            b = True
            c += 1
    print(a, ' ', c)
else:
    if(a > 31):
        print(a - 31, ' ', 2)
    else:
        print(a, ' ', 1)