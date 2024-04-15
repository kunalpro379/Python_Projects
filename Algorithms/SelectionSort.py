

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [12, 543, 75, 2, 75, 67, 67, 4, 54, 999, 46, 252, 1, 384, 48, 97, 0, 3]
print("Initial array:", arr)
selection_sort(arr)
print("Array after Selection Sort:", arr)
