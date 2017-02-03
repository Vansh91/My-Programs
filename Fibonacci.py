def fib():
    a, b = 0, 1
    fib_series = []

    for i in range(11):
        fib_series.append(a)
        a, b = b, a + b

    print(fib_series)

fib()
