# Selection Sort

not_sorted_array = [2, 8, 5, 3, 9, 4, 1]
print("Before: ", not_sorted_array)

# Time Complexity:      θ(n ** 2), Ω(n ** 2)
# Space Complexity :    O(1)
def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array

print("After:  ", selection_sort(not_sorted_array.copy()))