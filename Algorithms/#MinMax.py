#MinMax.py
def find_min_max(arr):
    if not arr:
        return None, None
    
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return min_val, max_val

if __name__ == "__main__":
    arr = [3, 5, 1, 9, 4, 7, 2]
    min_val, max_val = find_min_max(arr)
    print("Minimum element:", min_val)
    print("Maximum element:", max_val)
