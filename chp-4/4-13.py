def find_max_guests(entry, exit):
    # sort entry and exit timings
    entry.sort()
    exit.sort()

    time = entry[0]  # track time of max guests
    guest_in = 1
    max_guests = 1
    i = 1  # pointer to entry
    j = 0  # pointer to exit
    while (i < len(entry) and j < len(entry)):
        # a guest enters before next exit time
        if entry[i] <= exit[j]:
            guest_in += 1
            # update max_guests and time if needed
            if guest_in > max_guests:
                max_guests = guest_in
                time = entry[i]
            # increment pointer to check next entry time
            i += 1
        # a guest leaves before next entry time
        else:
            guest_in -= 1
            j += 1

    return time, max_guests
