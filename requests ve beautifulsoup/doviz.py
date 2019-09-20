import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.doviz.com/"

response = requests.get(url)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

dolar_deger = soup.find_all("span",{"class":"value"})[1]
dolar_deger = dolar_deger.text
dolar_deger = dolar_deger.replace(",",".")
dolar_deger = float(dolar_deger)

dolar_miktar = 12570
print("dolar güncel kuru:",dolar_deger)
print("önceki miktar",dolar_miktar,"$","~","Türk Lirası karşılığı",dolar_deger*dolar_miktar,"₺")

if (dolar_deger <= 5.80 and dolar_deger >= 5.60):
    dolar_miktar += 1000
    print(dolar_deger,"kurundan 1000$ satın alındı.","tarih:",datetime.now(),"\n")
elif dolar_deger >= 5.81:
    dolar_miktar -= 3000

print("güncel miktar",dolar_miktar,"$","~","Türk Lirasi karşılığı",dolar_deger*dolar_miktar,"₺")

