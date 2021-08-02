import math


def sort(arr):
    new_arr = []
    while len(arr) > 0:
        new_arr.append(arr[0])
        arr = arr[1:]
        recursion_heap_making(arr)
    for i in range(0, len(new_arr)//2):
        new_arr[len(new_arr)-i-1], new_arr[i] = new_arr[i], new_arr[len(new_arr)-i-1]
    return new_arr



def heap_making(arr):
    for j in range(0, len(arr) // 2):
        for i in range(0, len(arr) // 2):
            left = i * 2 + 1
            right = left + 1
            if len(arr) > right:
                if arr[i] < arr[left]:
                    arr[i], arr[left] = arr[left], arr[i]
                if arr[i] < arr[right]:
                    arr[i], arr[right] = arr[right], arr[i]
            else:
                if arr[i] < arr[i * 2 + 1]:
                    arr[i], arr[i * 2 + 1] = arr[i * 2 + 1], arr[i]
    return arr


def recursion_heap_making(arr):
    mid = len(arr) // 2
    if len(arr) > 0:
        for j in range(int(math.log(len(arr), 2))):
            for i in range(mid, len(arr)):
                if arr[i] > arr[(i - 1) // 2]:
                    arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
            arr[0:len(arr) // 2] = recursion_heap_making(arr[0:len(arr) // 2])

    return arr



a = [23, 13, 7, 12, 1, 1, 4, 9]
print(all(a))
print(sort(a))