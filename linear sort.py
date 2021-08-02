def linear_sort(arr):
    for i in range(1, len(arr)):
        n = 0
        while i-n >= 0:
            if arr[i-n] < arr[i-n-1] and i-n-1 != -1:
                arr[i-n-1], arr[i-n] = arr[i-n], arr[i-n-1]
            else:
                break
            n += 1
    return arr



print(linear_sort([3, 7, 1, 8, 12, 0]))