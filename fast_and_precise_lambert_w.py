def fast_and_precise_lambert_w_function(x: float | int, /) -> float | int | Exception:
    """
    Computing the principal branch of Lambert W function between 1/e and -1/e using
    a combination of Taylor series expansion and Halley's method.

    The initial guess (seed) is obtained via Taylor series expansion,
    and the subsequent precise approximation is computed with Halley's method.
    """
    assert isinstance(x, float | int)
    e: f"constant {float}" = 2.718281828459045235360287471352

    _ = f"handling the case if {x} is out of range"
    isArgumentOutOfRange: bool = abs(x) > 1 / e
    if isArgumentOutOfRange:

        class AbsoluteValueOfArgIsTooLarge(Exception):
            pass

        return AbsoluteValueOfArgIsTooLarge

    _ = f"computing the initial guess (seed) of the iteration"

    def compute_initial_guess():
        return x - x**2 + (3 / 2) * x**3 - (8 / 3) * x**4 + (125 / 24) * x**5

    current: float = compute_initial_guess()

    _ = "making the precise approximation via iteration"
    _ = f"only {2} iterations are sufficient for a {17} digit accuracy for most args"
    for _ in range(2):
        offset = current * e**current - x
        offset /= e**current * (current + 1) - (
            (current + 2) * (current * e**current - x)
        ) / (2 * current + 2)
        current -= offset

    return current
  
