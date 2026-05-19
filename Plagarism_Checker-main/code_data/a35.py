def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Data written to {filename}")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def main():
    filename = "example.txt"
    data = "Hello, this is a test file.\nThis file contains multiple lines of text."
    write_to_file(filename, data)

    print("\nReading from the file:")
    content = read_from_file(filename)
    if content:
        print(content)

if __name__ == "__main__":
    main()
