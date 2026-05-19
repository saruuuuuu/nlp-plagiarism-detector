def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    n = 10
    print(f"Fibonacci sequence up to {n} elements:")
    print(fibonacci(n))

if __name__ == "__main__":
    main()
