def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content saved to {filename}.")

def main():
    print("Welcome to the Simple Markdown Editor!")
    content = ""
    
    while True:
        line = input("Enter a line of text (or type 'save' to save, 'exit' to exit): ")
        if line.lower() == 'save':
            filename = input("Enter filename to save (e.g., output.md): ")
            save_to_file(content, filename)
        elif line.lower() == 'exit':
            print("Exiting the editor.")
            break
        else:
            content += line + "\n"
            print("Line added to content.")

if __name__ == "__main__":
    main()
