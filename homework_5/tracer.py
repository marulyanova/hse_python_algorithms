import inspect


def trace_recursion(func):
    def wrapper(*args, **kwargs):
        stack = inspect.stack()
        depth = len([frame for frame in stack[1:] if frame.function == func.__name__])

        print(f"{'  ' * depth}-> {func.__name__}(args={args}, kwargs={kwargs})")

        res = func(*args, **kwargs)

        print(f"{'  ' * depth}<- {func.__name__}(args={args}, kwargs={kwargs}) = {res}")

        return res

    return wrapper


@trace_recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


@trace_recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("Tracing Factorial of 7...", end="\n\n")
    print("\nFactorial of 7:", factorial(7), end="\n\n----------------\n\n")

    print("Tracing Fibonacci of 6...", end="\n\n")
    print("\nFibonacci of 6:", fibonacci(6))
