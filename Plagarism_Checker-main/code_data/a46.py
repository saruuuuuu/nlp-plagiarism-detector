import re

def is_valid_url(url):
    pattern = r'^(http|https)://[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}'
    return re.match(pattern, url) is not None

def main():
    while True:
        url = input("Enter a URL to validate (or type 'exit' to quit): ")
        if url.lower() == 'exit':
            break
        if is_valid_url(url):
            print(f"{url} is a valid URL.")
        else:
            print(f"{url} is not a valid URL.")

if __name__ == "__main__":
    main()
