def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while start < end:
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        start += 1
    return arr

print(cocktail_sort([12, 47, 46, 54, 19, 0]))