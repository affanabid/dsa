def recursive_binary_search(list, start, end, key):
    if start <= end:
        mid = (start + end) // 2
        if list[mid] == key:
            return mid
        
        elif list[mid] < key:
            return recursive_binary_search(list, mid+1, end, key)

        else:
            return recursive_binary_search(list, start, mid-1, key)

    else:
        return -1
    
def main():
    list = [13,28,31,46,59]
    key = 28
    result = recursive_binary_search(list, 0, len(list)-1, key)
    if result != -1:
        print(f"Key found at index: {result}")
    else:
        print("Key not found in the given list.")

if __name__ == "__main__":
    main()