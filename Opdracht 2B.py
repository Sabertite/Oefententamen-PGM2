def only_even_lc(L):

    return [number for number in L if number % 2 == 0]

assert only_even_lc([0, 1, 2, 3, 4]) == [0, 2, 4]