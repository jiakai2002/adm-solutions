import heapq


def find_second_largest(lst):
    heap = [-i for i in lst]
    heapq.heapify(heap)  # cost = 2n
    print(heap)
    second = -heap[2]
    third = -heap[1]
    return second, third


print(find_second_largest([3, 45, 16, 7, 11, 4, 2]))
