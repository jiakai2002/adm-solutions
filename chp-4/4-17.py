import heapq


def find_k_smallest(set, k):
    result = []
    heapq.heapify(set)
    for i in range(k):
        result.append(heapq.heappop(set))
    return result


print(find_k_smallest([5, 12, 1, 3], 2))
