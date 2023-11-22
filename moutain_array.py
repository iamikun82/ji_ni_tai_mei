def mountain_array(arr):
    if len(arr) < 3:
        return False
    max_word = max(arr)
    print(max_word)
    print(arr.index(max_word))
    for left in range(0, arr.index(max_word)-1):
        if arr[left] >= arr[left+1]:
            return False
    for right in range(len(arr)-1, arr.index(max_word)+3, -1):
        if arr[right] >= arr[right-1]:
            return False

    return True

arr = [2, 1, 3, 7]

print(mountain_array(arr))