def fib(n: int) -> int:
    # base case
    if n < 0:
        raise ValueError("Negatives not handled")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main() -> None:
    # F = fib(-1)
    # print(F)
    F = fib(0)
    print(F)
    F = fib(1)
    print(F)
    F = fib(2)
    print(F)
    F = fib(3)
    print(F)
    F = fib(4)
    print(F)
    F = fib(5)
    print(F)


if __name__ == "__main__":
    main()
