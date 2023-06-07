import heapq


def merge_lists(lists):
    result = []
    heapq.heapify(lists)
    while any(lists):
        min_list = heapq.heappop(lists)
        result.append(min_list[0])
        if min_list[1:]:
            heapq.heappush(lists, min_list[1:])
    return result


lists = [[1, 2, 13], [4, 9, 81], [21, 24, 47, 30]]
print(merge_lists(lists))
