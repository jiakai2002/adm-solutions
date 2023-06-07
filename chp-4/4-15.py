def find_max_point(intervals):
    # separate and sort left endpoints and right enpoints
    left = sorted([i[0] for i in intervals])
    right = sorted([i[1] for i in intervals])
    point = left[0]
    count = 0
    max_count = 0
    i = 0  # pointer to left endpoints
    j = 0  # pointer to right endpoints
    while (i < len(left) and j < len(right)):
        # intervals overlap
        if left[i] <= right[j]:
            count += 1
            # update max_count and point if needed
            if count > max_count:
                max_count = count
                point = left[i]
                print(point, max_count)
            # move pointer to next left endpoint
            i += 1
        # intervals do not overlap
        # reset count and increment i to find next point
        else:
            count = 0
            i += 1
    return point, max_count
