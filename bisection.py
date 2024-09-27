def bisect(f, a, b, tol=1e-9):

    """
    f: a function that takes a single argument
    a: lower bound of the interval
    b: upper bound of the interval
    tol: tolerance for the stopping criterion
    """

    # Bisection Method [By Bottom Science]

    while (b-a) > tol:
        c = (a+b) / 2
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a+b)/2

# Test
def f(x):
    return x**2 - x - 1

root = bisect(f, 0, 2, 1e-6)
print(root)

