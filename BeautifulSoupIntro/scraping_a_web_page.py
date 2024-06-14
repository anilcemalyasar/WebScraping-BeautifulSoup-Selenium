from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.example.com")
if result.status_code == 200:
    html = result.content
    soup = BeautifulSoup(html, "html.parser")
    print(soup.find("h1").text)

