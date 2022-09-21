import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "YOUR_PRODUCT_URL"
MAIL = "YOUR_MAIL_ID"
PASSWORD = "YOUR_MAIL_ID_PASSWORD"
EXCEPTED_PRICE = YOUR_EXCEPTED_PRICE
HEADER = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ta;q=0.6"
}

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").text.split("$")[1])
print(f"Current Price :  {price}")

if price <= EXCEPTED_PRICE:
    connect = smtplib.SMTP("smtp.gmail.com", port=587)
    connect.starttls()
    connect.login(user=MAIL, password=PASSWORD)
    connect.sendmail(from_addr=MAIL, to_addrs=MAIL, msg=f"Subject:PRICE DROP ALERT!!! \n\n Price has droped below {EXCEPTED_PRICE}")
    connect.close()
