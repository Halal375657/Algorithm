'''
    Complixity:-O(n)
'''

def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i

    return -1

def test_linear_search():
    assert -1 == linear_search([1, 3, 5, 6], 10)
    assert 3 == linear_search([1, 3, 5, 6], 6)
    assert -1 == linear_search([], 3)


