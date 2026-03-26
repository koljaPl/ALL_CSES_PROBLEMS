from algorithms.sorting.quick_sort import quick_sort, quick_sort_pythonic

def test_quick_sort(array_to_sort):
    expected = sorted(array_to_sort)
    # Твоя реализация требует передачи low и high.
    # Защищаемся от ошибки пустого массива, где len() - 1 будет -1
    if array_to_sort:
        quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
    assert array_to_sort == expected

def test_quick_sort_pythonic(array_to_sort):
    expected = sorted(array_to_sort)
    result = quick_sort_pythonic(array_to_sort)
    assert result == expected