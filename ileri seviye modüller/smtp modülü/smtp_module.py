import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

"""
SMTP Modülü ile mail gönderme

İlk olarak daha az güvenli uygulamalar için öncelikle aşağıdaki linke gidiyoruz ve güvenliği
kaldırıyoruz.

https://myaccount.google.com/lesssecureapps

"""

mesaj = MIMEMultipart()
mesaj["From"] = "Mesajı gönderen e-mail"
mesaj["To"] = "Mesajın gittiği e-mail"
mesaj["Subject"] = "Mesajın konusu"

yazi = """

mesaj bölümü

"""

mesaj_govdesi= MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("e-posta adresi","e-posta şifresi")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail başarıyla gönderildi.")
except:
    sys.stderr.write("Bir şeyler yanlış gitti.")
    sys.stderr.flush()





