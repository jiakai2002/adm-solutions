# (a): set n to 1/2
# (b): set n to 1/4


def find_majority_element(lst, n):
    freq_dict = {}
    result = []
    for i in lst:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    for k, v in freq_dict.items():
        if v > n * len(lst):
            result.append(k)
    return result
