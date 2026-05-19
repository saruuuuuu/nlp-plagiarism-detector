def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Please check the file path.")

def main():
    print("Welcome to the Text File Reader!")
    
    while True:
        file_path = input("Enter the path of the text file to read (or type 'exit' to quit): ")
        if file_path.lower() == 'exit':
            print("Exiting the text file reader.")
            break
        
        read_file(file_path)

if __name__ == "__main__":
    main()
