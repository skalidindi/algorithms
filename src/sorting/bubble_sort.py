from typing import List


def bubble_sort(arr: List[int]):
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def main() -> None:
    test_data = [12, 11, 13, 5, 6, 7]
    print("Original array:", test_data)
    bubble_sort(test_data)
    print("Sorted array:  ", test_data)


if __name__ == "__main__":
    main()
