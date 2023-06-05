import heapq

# (a)


def find_pair_a(lst):
    x = max(lst)
    y = min(lst)
    return x, y


# (b)


def find_pair_b(lst):
    x = lst[-1]
    y = lst[0]
    return x, y


# (c)


def find_pair_c(lst):
    sorted_lst = []
    heapq.heapify(lst)
    while lst:
        sorted_lst.append(heapq.heappop(lst))
    min_info = [float("inf"), 0, 0]
    for i in range(len(sorted_lst) - 1):
        diff = sorted_lst[i + 1] - sorted_lst[i]
        if diff < min_info[0]:
            print("hi")
            min_info[0] = diff
            min_info[1] = sorted_lst[i]
            min_info[2] = sorted_lst[i + 1]
    return min_info[1], min_info[2]


# (d)


def find_pair_d(sorted_lst):
    min_info = [float("inf"), 0, 0]
    for i in range(len(sorted_lst) - 1):
        diff = sorted_lst[i + 1] - sorted_lst[i]
        if diff < min_info[0]:
            print("hi")
            min_info[0] = diff
            min_info[1] = sorted_lst[i]
            min_info[2] = sorted_lst[i + 1]
    return min_info[1], min_info[2]
