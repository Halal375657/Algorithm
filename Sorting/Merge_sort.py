'''
    Complixity:-O(n)
'''

def marge(a, b):
    marged_list = []
    length_a, length_b = len(a), len(b)
    i, j = 0, 0

    while i < length_a and j < length_b:
        if a[i] < b[j]:
            marged_list.append(a[i])
            i += 1
        else:
            marged_list.append(b[j])
            j += 1
    marged_list += a[i:]
    marged_list += b[j:]
    return marged_list

'''
def marge(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = marge(L[:mid])
    right = marge(L[mid:])
    return marge(left, right)
'''

def test_marge():
    a, b = [1, 4], [2, 3]
    assert marge(a, b) == [1, 2, 3, 4]
    a, b = [1, 3, 4, 6], [2, 5, 9, 10]
    assert marge(a, b) == [1, 2, 3, 4, 5, 6, 9, 10]
    a, b = [],[]
    assert marge(a, b) == []
    a, b = [], [1]
    assert marge(a, b) == [1]
    a, b = [1], [1]
    assert marge(a, b) == [1,1]

if __name__ == "__main__":
    scenarios = [
        {"a": [1], "b": [2], "expected": [1, 2]},
        {'a': [2], 'b': [1], 'expected': [1, 2]},
        {'a': [], 'b': [1, 2], 'expected': [1, 2]},
        {'a': [1, 3], 'b': [], 'expected': [1, 3]},
        {'a': [1, 3, 5, 6], 'b': [2, 4, 7, 8], 'expected': [1, 2, 3, 4, 5, 6, 7, 8]},
        {'a': [1], 'b': [2, 3, 4], 'expected': [1, 2, 3, 4]},
        ]
    for item in scenarios:
        marged_list = marge(item['a'], item['b'])

        try:
            assert item['expected'] == marged_list
        except AssertionError:
            print("Output didn't match expected output")
            print("expected:", item['expected'])
            print("got", marged_list)
