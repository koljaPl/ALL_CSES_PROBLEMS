from algorithms.sorting.merge_sort import merge_sort_v1, merge_sort_v2

def test_merge_sort_v1(array_to_sort):
    expected = sorted(array_to_sort)
    result = merge_sort_v1(array_to_sort)
    assert result == expected

def test_merge_sort_v2(array_to_sort):
    expected = sorted(array_to_sort)
    # merge_sort_v2 возвращает deque, поэтому оборачиваем в list()
    result = list(merge_sort_v2(array_to_sort))
    assert result == expected