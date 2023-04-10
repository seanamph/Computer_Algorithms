def horner(c, x):
    """
    Evaluate a polynomial using Horner's rule.

    Args:
        c (list[float]): A list of coefficients representing a polynomial in descending order of degree.
        x (float): The value at which to evaluate the polynomial.

    Returns:
        float: The value of the polynomial at x.
    """
    n = len(c)
    result = c[n-1]
    for i in range(n-2, -1, -1):
        result = result * x + c[i]
    return result

c = [3, 2, -1, 4]
x = 2
print(horner(c, x))