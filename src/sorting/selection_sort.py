from typing import List


def selection_sort(arr: List[int]):
    n = len(arr)
    for i in range(0, n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main() -> None:
    test_data = [12, 11, 13, 5, 6, 7]
    print("Original array:", test_data)
    selection_sort(test_data)
    print("Sorted array:  ", test_data)


if __name__ == "__main__":
    main()
