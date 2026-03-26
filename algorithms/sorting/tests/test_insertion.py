from algorithms.sorting.insertion_sort import insertion_sort_v1, insertion_sort_v2

def test_insertion_sort_v1(array_to_sort):
    expected = sorted(array_to_sort)
    insertion_sort_v1(array_to_sort) # Функция меняет массив, но возвращает None
    assert array_to_sort == expected

def test_insertion_sort_v2(array_to_sort):
    expected = sorted(array_to_sort)
    insertion_sort_v2(array_to_sort)
    assert array_to_sort == expected