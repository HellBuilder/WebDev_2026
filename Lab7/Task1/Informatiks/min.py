def min(array):
    a = array[len(array) - 1]
    for i in range(len(array)):
        if(a > array[i]):
            a = array[i]
    return a



a = [int(num) for num in input().split()]
print(min(a))