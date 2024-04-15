#Binaryseach.py
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    target = 11
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")
