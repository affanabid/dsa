def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key
    
    return array

array = [5,2,8,3,6]
print(insertionSort(array))