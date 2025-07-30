from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into a single sorted list."""
    merged: List[int] = []
    i, j = 0, 0

    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements if any
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort(arr: List[int]) -> List[int]:
    """Sort the array using merge sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def main() -> None:
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)


if __name__ == "__main__":
    main()
