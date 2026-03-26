from algorithms.sorting.heap_sort import heap_sort

def test_heap_sort_v1(array_to_sort):
    expected = sorted(array_to_sort)
    heap_sort(array_to_sort)
    assert array_to_sort == expected