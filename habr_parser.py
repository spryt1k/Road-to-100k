import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/news/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h2")
for i, title in enumerate(titles):
    print(f"{i+1}. {title.text.strip()}")
