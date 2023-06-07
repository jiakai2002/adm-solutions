def merge_pairs(pairs):
    pairs.sort(key=lambda i: i[0])
    result = [pairs[0]]
    for start, end in pairs:
        last_end = result[-1][1]
        if start <= last_end:
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])
    return result


print(merge_pairs([([1, 3]), [2, 6], [2, 9], [10, 12]]))
