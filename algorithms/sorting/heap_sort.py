# Heap Sort

not_sorted_array = [2, 8, 5, 3, 9, 4, 1]
print("Before: ", not_sorted_array)

# Time Complexity:      θ(n log n), Ω(n log n)
# Space Complexity :    O(log n)
def heap_sort(array):
    n = len(array)
    build_max_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        n = n - 1
        heapify(array, 0, n)

    return array

# Time: O(n)
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, i, n)

# Time: O(log n), called n - 1 times
def heapify(array, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and array[left] > array[largest]:
        largest = left
    else:
        largest = i

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, largest, n)


print("After:  ", heap_sort(not_sorted_array.copy()))