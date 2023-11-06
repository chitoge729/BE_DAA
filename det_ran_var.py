import random

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    equal = []
    right = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    return deterministic_quick_sort(left) + equal + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = []
    equal = []
    right = []

    for i, element in enumerate(arr):
        if element < pivot:
            left.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            right.append(element)

    return randomized_quick_sort(left) + equal + randomized_quick_sort(right)

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    user_input = input("Enter the space-separated elements: ")
    arr = list(map(int, user_input.split()))

    sorted_arr_det = deterministic_quick_sort(arr.copy())
    sorted_arr_rand = randomized_quick_sort(arr.copy())

    print("Deterministic Quick Sort:")
    print("Sorted Array: ", sorted_arr_det)

    print("\nRandomized Quick Sort:")
    print("Sorted Array: ", sorted_arr_rand)
