def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def main():
    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to generate (or -1 to exit): "))
            if n == -1:
                break
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            fib_sequence = generate_fibonacci(n)
            print("Fibonacci Sequence:", fib_sequence)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
