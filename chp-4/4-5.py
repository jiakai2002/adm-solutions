import heapq


def find_mode(lst):
    sorted_lst = []
    heapq.heapify(lst)
    while lst:
        sorted_lst.append(heapq.heappop(lst))
    mode = None
    max_count = 0
    count = 1
    for i in range(len(sorted_lst) - 2):
        if sorted_lst[i] == sorted_lst[i + 1]:
            count += 1
            if count > max_count:
                mode = sorted_lst[i]
                max_count = count
        else:
            count = 1
    return mode


print(find_mode([1, 1, 3, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 7, 8, 9]))
