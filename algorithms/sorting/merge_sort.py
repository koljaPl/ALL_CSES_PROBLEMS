# Merge Sort (my favorite method - divide and conquer)

not_sorted_array = [2, 8, 5, 3, 9, 4, 1]
print("Before:   ", not_sorted_array)

# Time Complexity:      θ(n log n), Ω(n log n)
# Space Complexity :    O(n) - для массива + O(log n) для стека рекурсии = итого O(n)
def merge_v1(left, right):
    array = []

    while left and right:
        if left[0] < right[0]:
            array.append(left[0])
            left.pop(0)
        else:
            array.append(right[0])
            right.pop(0)

    while left:
        array.append(left[0])
        left.pop(0)

    while right:
        array.append(right[0])
        right.pop(0)

    return array

def merge_sort_v1(array):
    n = len(array)

    if n <= 1:
        return array

    left = merge_sort_v1(array[: n // 2])
    right = merge_sort_v1(array[n // 2:])

    return merge_v1(left, right)

print("After V1: ", merge_sort_v1(not_sorted_array.copy()))


# Let's do tiny optimization with deque for deleting first element with O(1) time
from collections import deque

# Time Complexity:      θ(n log n), Ω(n log n)
# Space Complexity :    O(n) - для массива + O(log n) для стека рекурсии = итого O(n)
def merge_v2(left, right):
    array = deque()

    while left and right:
        if left[0] < right[0]:
            array.append(left.popleft())
        else:
            array.append(right.popleft())

    array.extend(left)
    array.extend(right)

    return array

def merge_sort_v2(array):
    n = len(array)

    if n <= 1:
        return deque(array)

    left = merge_sort_v2(array[: n // 2])
    right = merge_sort_v2(array[n // 2:])

    return merge_v2(left, right)

print("After V2: ", list(merge_sort_v2(not_sorted_array.copy())))
