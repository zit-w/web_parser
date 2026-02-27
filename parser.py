import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

def parse_news():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.select(".titleline a")

    print("Latest news:\n")
    for i, title in enumerate(titles[:10], 1):
        print(f"{i}. {title.text}")

if __name__ == "__main__":
    parse_news()
