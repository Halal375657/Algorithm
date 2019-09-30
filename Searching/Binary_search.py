'''
    Complixity:- O(log n)
'''
def binary_search(L, item):
    left, right = 0, len(L) -1

    while left <= right:
        mid = (left+right) // 2

        if L[mid] == item:
            return mid

        if L[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return -1


#test binary_search()
def test_binary_search():
    assert -1 == binary_search([1, 3, 5, 8], 10)
    assert 2  == binary_search([1, 3, 4, 8], 4)
    assert -1 == binary_search([], 4)
