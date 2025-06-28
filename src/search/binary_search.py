def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found the target at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found


# ---------------------------
# 🔬 Example usage:
# ---------------------------
def main():
    print(binary_search([1, 2, 3, 4, 5, 7, 9, 30, 50], 30))
