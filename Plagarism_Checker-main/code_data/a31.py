from bs4 import BeautifulSoup
import requests

def get_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = [title.get_text() for title in soup.find_all('h2')]
        return titles
    else:
        print("Failed to retrieve the webpage.")
        return []

def main():
    url = "https://example.com"  # Replace with a valid URL for testing
    print(f"Scraping titles from: {url}")
    titles = get_titles(url)
    if titles:
        print("Titles found:")
        for title in titles:
            print(f"- {title}")
    else:
        print("No titles found.")

if __name__ == "__main__":
    main()
