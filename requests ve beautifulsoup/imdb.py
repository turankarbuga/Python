import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

print("top 250 filmleri görmek için 0 yazınız.")
deger = float(input("En düşük imdb puanı:"))

basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})



for baslik,rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if float(rating) >= deger:
        print(baslik,rating)
