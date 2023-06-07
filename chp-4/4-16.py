def find_segments(segments, interval):
    segments.sort(key=lambda i: i[0])
    count = 0
    start = segments[0]
    end = segments[0] - 1
    for seg in segments:
        if seg[0] <= start:
            end = seg[1]
        else:
            start = end
