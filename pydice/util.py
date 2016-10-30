def group(lst, n):
    for i in range(0, len(lst), n):
        yield tuple(lst[i:i+n])
