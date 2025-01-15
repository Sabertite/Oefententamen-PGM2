def only_even_rec(L):

    if len(L) == 0:
        return []
    elif L[0] % 2 == 0:
        return [L[0]] + only_even_rec(L[1:])
    else:
        return only_even_rec(L[1:])

assert only_even_rec([0, 1, 2, 3, 4]) == [0, 2, 4]