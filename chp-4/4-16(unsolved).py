def find_segments(segments, interval):
    segments.sort(key=lambda i: i[0])
    print(segments)
    count = 1
    start = interval[0]
    end = interval[0] - 1
    print("init", start, end)
    for seg in segments:
        # segment starts before/at current interval, improve end if possible
        if seg[0] <= start:
            end = max(end, seg[1])
            print("improve", start, end)
        else:
            # previous segment end maximised, pick new segment
            start = end
            end = max(end, seg[1])
            print("pick new", seg)
            count += 1
            # cannot move or interval covered
            if seg[0] > end or end >= interval[1]:
                break
    if end < interval[1]:
        return False

    return count


print(find_segments([[0, 1], [0, 3], [2, 4],
      [2, 10], [3, 7], [6, 11]], [3, 11]))
