import heapq


def find_h_index(cit):
    sorted_cit = []
    heapq.heapify(cit)
    while cit:
        sorted_cit.append(heapq.heappop(cit))
    h = None
    count = 1
    for i in range(len(sorted_cit) - 2):
        if sorted_cit[i] == sorted_cit[i + 1]:
            count += 1
            if count == sorted_cit[i]:
                h = sorted_cit[i]
        else:
            count = 1
    return h


print(find_h_index([1, 2, 2, 2, 3, 3, 4, 4, 4]))
