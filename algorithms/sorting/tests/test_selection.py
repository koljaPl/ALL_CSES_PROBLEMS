from algorithms.sorting.selection_sort import selection_sort

def test_selection_sort_v1(array_to_sort):
    expected = sorted(array_to_sort)
    selection_sort(array_to_sort)
    assert array_to_sort == expected