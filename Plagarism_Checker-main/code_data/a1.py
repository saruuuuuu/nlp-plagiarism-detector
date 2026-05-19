def dynamic_hello_world(times):
    for i in range(1, times + 1):
        print(f"Hello World - Message {i}")

def main():
    times = 5
    print(f"Displaying 'Hello World' {times} times dynamically:")
    dynamic_hello_world(times)

if __name__ == "__main__":
    main()
