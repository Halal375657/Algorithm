'''
    Space Complixity:- O(m)- Here, m is max element of given list.
    Time Complixity:- O(n)- Here, n is number of element of given list.
'''

class Sort:
    def count_sort(self, L):
        m = max(L)+1
        arr_list = [False]*m

        for i in L:
            arr_list[i] += 1

        for i in range(m):
            if arr_list[i]:
                print((str(i)+' ')*arr_list[i], end='')


if __name__ == "__main__":
    sort = Sort()
    L = [2, 5, 2, 1, 6, 5, 3, 4, 8, 10, 2, 4]
    print("After sort:", end = ' ')
    sort.count_sort(L)

