def merge_sort(arr):
    if len(arr) > 1:
        # 将数组分成两半
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        # 递归排序两个子数组
        merge_sort(left_half)
        merge_sort(right_half)
        # 合并两个已排序的子数组
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 使用示例：
arr = [8,4,5,2,9,3,6,1,7]
merge_sort(arr)
print("排序后的数组:", arr)