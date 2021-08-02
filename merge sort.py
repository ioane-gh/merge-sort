def merge_sorting(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) > 1:
        mid = len(arr) // 2
        working_arr1 = arr[0:mid]
        working_arr2 = arr[mid:]
        working_arr1 = merge_sorting(working_arr1)
        working_arr2 = merge_sorting(working_arr2)
        
        i = 0
        j = 0
        k = 0
        if working_arr1 is not None and working_arr2 is not None:
            while len(working_arr1) > i and len(working_arr2) > j:
                if working_arr1[i] > working_arr2[j]:
                    arr[k] = working_arr2[j]
                    k += 1
                    j += 1
                else:
                    arr[k] = working_arr1[i]
                    k += 1
                    i += 1
            if len(working_arr1) > i:
                arr[k] = working_arr1[i]
                i += 1
                k += 1
            if len(working_arr2) > j:
                arr[k] = working_arr2[j]
                j += 1
                k += 1
        return arr


print(merge_sorting([12, 1, 42, 7, 23, 6]))
