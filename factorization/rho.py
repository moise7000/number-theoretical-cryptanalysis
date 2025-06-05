from math import gcd


def pollard_rho(n, f=lambda x, n: (x * x + 1) % n, x1=1, max_iterations=10000):
    x = x1
    y = x1
    sequence = [(1, x1)]
    i = j = 1

    for iteration in range(2, max_iterations + 2):
        x = f(x, n)
        y = f(f(y, n), n)

        sequence.append((iteration, x))

        d = gcd(abs(x - y), n)
        print(f"Iteration {iteration - 1}: x = {x}, y = {y}, gcd(|x - y|, n) = {d}")

        if d == n:
            return sequence, None, None, f"Failure : cycle found (d = n = {n})"
        elif d > 1:
            return sequence[:iteration], iteration - 1, 2 * (iteration - 1), d

    return sequence, None, None, "No factors found in the given iterations"



if __name__ == "__main__":
    n = int(input("Enter an integer n to factor : "))

    sequence, i, j, result = pollard_rho(n)

    print("\n--- Sequence x_k (till x_j) ---")
    for index, value in sequence:
        print(f"x_{index} = {value}")

    print("\n--- Results ---")
    if isinstance(result, int):
        print(f"Factor found : {result} avec x_i = x_{i}, x_j = x_{j}")
    else:
        print(result)
