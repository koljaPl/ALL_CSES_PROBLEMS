import pytest

TEST_ARRAYS = [
    [],
    [1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [-5, -1, -9, 0, 4, 2],
    [2, 8, 5, 3, 9, 4, 1],
]

# ids используются для красивого отображения названий тестов в консоли
TEST_IDS = [
    "empty", "single", "already_sorted", "reversed",
    "duplicates", "negatives", "random"
]

@pytest.fixture(params=TEST_ARRAYS, ids=TEST_IDS)
def array_to_sort(request):
    """
    Эта фикстура будет "кормить" каждый тест каждым массивом из списка.
    ОБЯЗАТЕЛЬНО возвращаем копию .copy(), так как некоторые твои
    алгоритмы сортируют in-place (изменяют исходный массив).
    """
    return request.param.copy()