from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")

simdi = datetime.now()
# print(datetime.ctime(simdi))
# print(datetime.strftime(simdi,"%Y %B %A"))


tarih = datetime(2019,9,8,17,30)
simdi = datetime.now()

fark = simdi - tarih
print(fark)