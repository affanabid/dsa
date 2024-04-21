def recursiveBinarySearch(array, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right ) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return recursiveBinarySearch(array, target, left, mid-1)
    
    else:
        return recursiveBinarySearch(array, target, mid+1, right)


array = [5,2,7,1,9]
target = 9
print(recursiveBinarySearch(array, target, 0, len(array)))