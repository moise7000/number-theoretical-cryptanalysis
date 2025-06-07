def modular_inverse(a: int, n: int) -> int:
    """
    Computes the modular inverse of a modulo n, i.e., x such that (a * x) % n == 1.
    Uses the Extended Euclidean Algorithm.

    :param a: integer whose inverse is to be computed
    :param n: the modulus
    :return: the inverse of a modulo n if it exists
    :raises ValueError: if the inverse does not exist (a and n are not coprime)
    """
    t, new_t = 0, 1
    r, new_r = n, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError(f"{a} has no inverse modulo {n} (not coprime with {n})")
    if t < 0:
        t += n

    return t

# Example usage:
if __name__ == "__main__":
    a = int(input("Enter an integer a: "))
    n = int(input("Enter the modulus n: "))
    try:
        inv = modular_inverse(a, n)
        print(f"The modular inverse of {a} modulo {n} is: {inv}")
    except ValueError as e:
        print(e)
