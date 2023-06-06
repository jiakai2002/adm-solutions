# (a) and (b) both can be done in O(n) time using hashtable
# hashtable implemented as a reverse dictionary in python


def check_sum(s, total):
    dict_s = {v: k for k, v in enumerate(s)}
    print(dict_s)
    for x in s:
        y = total - x
        if y != x and dict_s.get(y):
            return True
    return False


print(check_sum([11, 7, 8, 6, 3, 5, 9, 1], 14))
