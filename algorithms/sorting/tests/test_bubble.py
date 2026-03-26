from algorithms.sorting.bubble_sort import bubble_sort_v1, bubble_sort_v2

def test_bubble_sort_v1(array_to_sort):
    expected = sorted(array_to_sort)
    bubble_sort_v1(array_to_sort) # Функция меняет массив, но возвращает None
    assert array_to_sort == expected

def test_bubble_sort_v2(array_to_sort):
    expected = sorted(array_to_sort)
    bubble_sort_v2(array_to_sort)
    assert array_to_sort == expected