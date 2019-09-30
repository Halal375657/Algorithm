'''
    Complixity:-
        max_heapify():- O(log n)
        build_max_heap():- O(n log n)
        heap_sort():- O(n log n)
        
'''

def left(i):
    return 2*i
def right(i):
    return 2*i+1

def parent(i):
    return i // 2

def is_max_heap(h):
    n = len(h) - 1

    for i in range(n, 1, -1):
        p = parent(i)
        if h[p] < h[i]:
            return False
    return True

def is_min_heap(h):
    n = len(h) - 1

    for i in range(n, 1, -1):
        p = parent(i)
        if h[p] > h[i]:
            return False
        return True

def max_heapify(heap, heap_size, i):
    l, r = left(i), right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)

def build_max_heap(heap):
    heap_size = len(heap) - 1

    for i in range(heap_size//2, 0, -1):
        max_heapify(heap, heap_size, i)

def heap_sort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1

    for i in range(heap_size, 1, -1):
        heap[1], heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)
        #print("Re:-", heap)

def get_maximum(heap):
    return heap[1]

def extract_max(heap, heap_size):
    max_item = heap[1]
    heap[1] = heap[heap_size]
    heap_size -= 1
    max_heapify(heap, heap_size, 1)
    return max_item

def insert_node(heap, heap_size, node):
    heap_size += 1
    heap[heap_size] = node
    i = heap_size

    while i > 1 and heap[i] > heap[parent(i)]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)

    return heap_size


if __name__=="__main__":
    print("=============== Heap sort ================")
    heap_ = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
    print("Before sorting:", heap_[1:])
    heap_sort(heap_)
    print("After sorting:", heap_[1:])

    #Test part
    print("\n\n\n\n================ Heap Check =================")
    heap = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
    print("Before sorting:", heap)
    print("Max heap:", get_maximum(heap))
    heap_size = len(heap) - 1
    print("Exract max number before sort:", extract_max(heap, heap_size))
    heap_sort(heap)
    print("After sorting:", heap)
    print("Extract max number after sort:", extract_max(heap, heap_size))
