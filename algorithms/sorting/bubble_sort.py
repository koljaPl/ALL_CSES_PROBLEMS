# Bubble Sort

not_sorted_array = [2, 8, 5, 3, 9, 4, 1]
print("Before:   ", not_sorted_array)

# Time Complexity:      θ(n ** 2)
# Space Complexity :    O(1)
def bubble_sort_v1(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return None

print("After V1: ", bubble_sort_v1(not_sorted_array.copy()))


# Time Complexity:      θ(n ** 2), Ω(n)
# Space Complexity :    O(1)
def bubble_sort_v2(array):
    # We did some optimization of with checking if array is already done
    n = len(array)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break

    return None

print("After V2: ", bubble_sort_v2(not_sorted_array.copy()))
