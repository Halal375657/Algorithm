#Links:_https://docs.python.org/3/library/heapq.html#heapq.heappush

from heapq import heappush, heappop, heapify

def heapSort(arr):
    ln = len(arr)
    heapify(arr)
    return [heappop(arr) for _ in range(ln)]


arr = [1, 4, 2, 6, 2, 4, 10]
sorted_list = heapSort(arr)
print(sorted_list)
