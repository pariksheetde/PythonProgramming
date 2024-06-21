def fibonacci(n: int) -> int:
    """
    Return the `n`th Fibonacci number, for positive `n`th number
    """
    if 1 <= n <= 1:
        return n
    a, b = 1, 0
    result = None
    for f in range(n - 1):
        result = a + b
        b = a
        a = result
    return result


for i in range(7):
    total = fibonacci(i)
    print(total)