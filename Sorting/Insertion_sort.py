'''
    Complixity:-O(n log n)
'''
def insertionSort(L):
    n = len(L)

    for i in range(1, n):
        item = L[i]
        j = i - 1

        while j >= 0 and L[j] > item:
            L[j+1] = L[j]
            j = j - 1
            L[j+1] = item
    return L


def test_insertionSort():
    arr_list = [[3, 2, 1, 4, 5], [], [2, 1, 2, -2], [1]]
    for arr in arr_list:
        assert sorted(arr) == insertionSort(arr)

