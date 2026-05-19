import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_mapping[short_url] = original_url
        return f"http://short.url/{short_url}"

    def retrieve_url(self, short_url):
        short_key = short_url.split('/')[-1]
        return self.url_mapping.get(short_key, "URL not found.")

def main():
    url_shortener = URLShortener()
    
    while True:
        original_url = input("Enter a URL to shorten (or 'exit' to quit): ")
        if original_url.lower() == 'exit':
            break
        
        short_url = url_shortener.shorten_url(original_url)
        print(f"Shortened URL: {short_url}")

        retrieve = input("Do you want to retrieve the original URL? (yes/no): ").lower()
        if retrieve == 'yes':
            print(url_shortener.retrieve_url(short_url))

if __name__ == "__main__":
    main()
