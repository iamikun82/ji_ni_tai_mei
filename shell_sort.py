def shell_sort(arr):
    n = len(arr)
    gap = n//2
    # 逐步减小增量直到 1
    while gap > 0:
        # 进行插入排序
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# 使用示例：
arr = [8,4,5,2,9,3,6,1,7]
shell_sort(arr)
print("排序后的数组:", arr)