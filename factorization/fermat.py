from math import isqrt


def fermat_factor(n, max_iterations=100000):
    if n % 2 == 0:
        print(f"{n} est pair → facteurs : 2 × {n // 2}")
        return 2, n // 2, "Succès immédiat"

    x = isqrt(n)
    if x * x < n:
        x += 1

    print(f"Start of Fermat factorization for n = {x}")
    print(f"Initial x = {x} (⎡√n⎤), we are looking for a y such that y² = x² - n be a perfect square\n")

    for iteration in range(1, max_iterations + 1):
        y2 = x * x - n
        y = isqrt(y2)
        print(f"[{iteration:4}] x = {x}, x² - n = {y2}, b = √{y2} = {y} → y² = {y * y}")

        if y * y == y2:
            p = x - y
            q = x + y
            if p == 1 or q == n:
                return None, None, f"Trivial factorization (p = 1 ou q = n) found after {iteration} iterations"
            return p, q, f"Success after {iteration} iterations"

        x += 1

    return None, None, f"No factor found after {max_iterations} iterations"


# Exemple d'utilisation
if __name__ == "__main__":
    n = int(input("Enter an odd integer to factor: "))
    p, q, message = fermat_factor(n)

    print("\n--- Results ---")
    if p and q:
        print(f"{n} = {p} × {q}")
    print(message)
