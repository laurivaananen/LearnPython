from collections import deque

elems = [5, 2, -1, 0, 3]

k = 3

def biggest_sub_array(elems, k):
    try:
        window = deque(elems[:k], k)
    except IndexError:
        return 0
    biggest_sum = sum(window)
    for elem in elems[k:]:
        window.append(elem)
        if len(window) == k:
            if sum(window) > biggest_sum:
                biggest_sum = sum(window)
    return biggest_sum

assert biggest_sub_array(elems, k) == 6
assert biggest_sub_array(elems, 100) == 0