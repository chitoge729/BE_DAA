def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    n = int(input("Enter the value of n to calculate the nth Fibonacci number: "))

    iterative_result = fibonacci_iterative(n)
    print(f"The {n}-th Fibonacci number (non-recursive) is: {iterative_result}")

    recursive_result = fibonacci_recursive(n)
    print(f"The {n}-th Fibonacci number (recursive) is: {recursive_result}")
