# Quick Sort

not_sorted_array = [2, 8, 5, 3, 9, 4, 1]
print("Before: ", not_sorted_array)

# Time Complexity:      Worst: θ(n ** 2), AVG: O(n log n), Best: Ω(n log n)
# Space Complexity :    Worst: O(n), Best: Ω(log n)
def partition(array, low, high):
    pivot = array[low]
    leftwall = low + 1

    for i in range(low + 1, high + 1):
        if array[i] < pivot:
            array[i], array[leftwall] = array[leftwall], array[i]
            leftwall += 1

    array[low], array[leftwall - 1] = array[leftwall - 1], array[low]

    return leftwall - 1

def quick_sort(array, low, high):
    if low < high:
        pivot_location = partition(array, low, high)
        quick_sort(array, low, pivot_location - 1)
        quick_sort(array, pivot_location + 1, high)

    return array


print("After:  ", quick_sort(not_sorted_array.copy(), 0, len(not_sorted_array) - 1))


# More pythonic style
def quick_sort_pythonic(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]

    return quick_sort_pythonic(left) + [pivot] + quick_sort_pythonic(right)

print("After (Pythonic):  ", quick_sort_pythonic(not_sorted_array.copy()))