import requests
from bs4 import BeautifulSoup

url = "https://www.obilet.com/"

response = requests.get(url)
print(response)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")


for i in soup.find_all("a"):
    print(i.get("href"))
    print("~.~.~.~.~.~.~.~")

