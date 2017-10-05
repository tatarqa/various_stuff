def get_factors(nr):
    sumarized_facotrs = 0
    factorial = 1
    while nr > 0:
        factorial *= nr
        nr -= 1
    while factorial > 1:
        sumarized_facotrs += factorial % 10
        factorial /= 10

    return sumarized_facotrs


print get_factors(100)
