from typing import List


def insertion_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def main() -> None:
    test_data = [12, 11, 13, 5, 6, 7]
    print("Original array:", test_data)
    insertion_sort(test_data)
    print("Sorted array:  ", test_data)


if __name__ == "__main__":
    main()
