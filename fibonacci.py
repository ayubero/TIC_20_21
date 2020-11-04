def fibonacci(num):
    fib = [0, 1]
    for i in range(num):
        if i <= 1:
            print(i)
        else:
            f = fib[i-2] + fib[i-1]
            fib.append(f)
            print(f)

fibonacci(100)
