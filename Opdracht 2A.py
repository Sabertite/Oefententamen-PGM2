def only_even_loop(L):

    lst = []

    for number in L:
        if number % 2 == 0:
            lst += [number]
        else:
            lst = lst
    return lst

assert only_even_loop([0, 1, 2, 3, 4]) == [0, 2, 4]
        