'''
    Complixity:- O(log n)
'''
def binary_search_recursive(li, item):
    mid = len(li)//2
    if li[mid] == item:
        return mid
    if mid == 0:
        return -1
    if li[mid] < item:
        return binary_search_recursive(li[mid:], item)
    if li[mid] > item:
        return binary_search_recursive(li[:mid], item)
        
def test_binary_search_recursive():
    li = [1, 4, 6, 7, 10, 15, 19, 23, 30, 40]
    assert binary_search_recursive(li, 0)  == -1
    assert binary_search_recursive(li, 50) == -1
    assert binary_search_recursive(li, 40) == 1
    assert binary_search_recursive(li, 1)  == 0
    assert binary_search_recursive(li, 40) == 1
    assert binary_search_recursive(li, 10) == 1

if __name__=='__main__':
    li = [1, 4, 6, 7, 10, 15, 19, 23, 30, 40]
    item = 40
    result = binary_search_recursive(li, item)
    if result is 1:
        print("Searching success",item,"in li")
    else:
        print("Searching unsuccess", item,"not in li")
    
