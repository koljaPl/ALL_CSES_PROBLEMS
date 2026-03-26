# Insertion Sort

not_sorted_array = [2, 8, 5, 3, 9, 4, 1]
print("Before:   ", not_sorted_array)

# Time Complexity:      θ(n²), Ω(n)
# Space Complexity :    O(1)
def insertion_sort_v1(array):
    # Для каждого числа если мы это числа не выходит меньше чем за нулевой индекс
    # и меньше чем его левый сосед то двигаем (свапаем) его на 1 позицию левее
    n = len(array)

    for i in range(1, n):
        j = i

        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array

print("After V1: ", insertion_sort_v1(not_sorted_array.copy()))


# Time Complexity:      θ(n²), Ω(n)
# Space Complexity :    O(1)
def insertion_sort_v2(array):
    # Мы сделали оптимизацию за счёт того что убрали довольно тяжелый swap и заменили его на shift
    # тоесть сдвиг с запоминанием
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

print("After V2: ", insertion_sort_v2(not_sorted_array.copy()))
