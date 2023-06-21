import heapq


def find_sum_k(S, T, k):
    sorted_S = []
    heapq.heapify(S)

    while S:
        sorted_S.append(heapq.heappop(S))

    def iter(x, current):
        if x == k:
            if (T - current) in sorted_S[x:]:
                return True
        for i in range(len(sorted_S) - x):
            iter(x + 1, current + sorted_S[i])

    return iter(1, 0)


print(find_sum_k([7, 2, 1, 5, 6], 10, 3))
