import heapq


def find_pair_c(lst):
    sorted_lst = []
    heapq.heapify(lst)
    while lst:
        sorted_lst.append(heapq.heappop(lst))
    pairs = []
    for i in range(len(sorted_lst) // 2 - 1):
        pairs.append([sorted_lst[i], sorted_lst[-i - 1]])
    return pairs
