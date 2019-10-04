#Complixity:- O(n^2)

def buble_sort(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1] < num:
                arr[i] = arr[i+1]
                arr[i+1] = num
                buble_sort(arr)
        except IndexError:
            return

if __name__ == "__main__":
    arr = [2, 5, 3, 1, 12, 39, 23, 20]
    buble_sort(arr)
    print(arr)
