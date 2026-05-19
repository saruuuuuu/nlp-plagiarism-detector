def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def main():
    num = 1234
    print(f"The sum of digits of {num} is: {sum_of_digits(num)}")

if __name__ == "__main__":
    main()
