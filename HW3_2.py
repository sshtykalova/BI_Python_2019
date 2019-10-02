def open_list(lst):
    for el in lst:
        try:
            yield from flat_list(el)
        except:
            yield el


def flat_list(array):
    return ([x for x in open_list(array)])
