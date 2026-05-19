import time

def start_stopwatch():
    print("Stopwatch started. Press Ctrl+C to stop.")
    start_time = time.time()
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"Elapsed Time: {elapsed_time:.2f} seconds", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        return elapsed_time

def main():
    while True:
        input("Press Enter to start the stopwatch (or type 'exit' to quit): ")
        if input == 'exit':
            print("Exiting the stopwatch.")
            break
        elapsed_time = start_stopwatch()
        print(f"Total elapsed time: {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
