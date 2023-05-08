def merge_sort(arr):
    print('merge_sort'+str(arr))
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        print('left1'+str(left))
        print('right1'+str(right))
        merge_sort(left)
        merge_sort(right)
        print('left2'+str(left))
        print('right2'+str(right))
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        print('arr'+str(arr))


arr = [4, 3, 2, 1, 5]
merge_sort(arr)
print(arr)