def sort_pairs(pairs):
    result = []
    for pair in pairs:
        if pair[1] == "red":
            result.append(pair)
            pairs.remove(pair)
    for pair in pairs:
        if pair[1] == "blue":
            result.append(pair)
            pairs.remove(pair)
    result.append(pairs)
    return result


print(sort_pairs([[1, "blue"], [3, "red"], [4, "blue"], [6, "yellow"], [9, "red"]]))
