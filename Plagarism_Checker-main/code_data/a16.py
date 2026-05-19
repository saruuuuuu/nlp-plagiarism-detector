def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def main():
    strings = ["A man, a plan, a canal, Panama", "Was it a car or a cat I saw?", "No lemon, no melon", "Hello"]
    for string in strings:
        print(f"Is '{string}' a palindrome? {'Yes' if is_palindrome(string) else 'No'}")

if __name__ == "__main__":
    main()
