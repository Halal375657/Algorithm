'''
    Complixity:- O(n^2)
'''

#I am here import the copy module for test method.
import copy

def buble_sort(L):
    length = len(L)

    for i in range(0, length):
        for j in range(0, length-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

#test buble_sort function
def test_buble_sort():
    L = [3, 5, 4, 2, 1]
    test_L = copy.copy(L)#Shallow Copy
    buble_sort(L)
    assert test_L != L
    assert [1, 2, 3, 4, 5] == L

if __name__ == "__main__":
    L = [1, 5, 2, 3, 4]
    print("Before sort:", L)
    buble_sort(L)
    print("After sort:",L)


