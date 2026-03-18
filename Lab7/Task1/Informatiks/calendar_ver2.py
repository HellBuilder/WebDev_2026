a = int(input())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = 1

for days in months:
    if a > days:
        a -= days
        month += 1
    else:
        break

print(a, month)