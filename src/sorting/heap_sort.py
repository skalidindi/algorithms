from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """Ensures the subtree rooted at index i is a max heap."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> None:
    """Performs in-place heap sort on the given list."""
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)


def main() -> None:
    test_data = [12, 11, 13, 5, 6, 7]
    print("Original array:", test_data)
    heap_sort(test_data)
    print("Sorted array:  ", test_data)


if __name__ == "__main__":
    main()
