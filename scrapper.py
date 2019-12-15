import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import smtplib
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url =input("Enter Link Of Any Amazon Product : ")

#url ='https://www.amazon.in/gp/product/B07HGJJ568?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=PST27DPVZV5GXNP4NN8K'

#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
# use headers in case of multiple checking..
def check_price():
 html=urllib.request.urlopen(url, context=ctx).read()

 soup=BeautifulSoup(html,'lxml')

 html=soup.prettify('utf-8')

 for divs in soup.findAll('div'):
     try:
        price = str(divs['data-asin-price'])
        #product_json['price'] = '$' + price couldn't get it to work i am noob
        break
     except:
        pass
 print(price)

 amount = input('Enter Desired Amount for comparator : ')
 if price == amount:

  send_mail()
def send_mail():
    

    s = smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()

    s.login("from or login mail", "2 step key or password")

    message = "Price is dropped"

    s.sendmail("first to mail","second to mail",message)

    s.quit()
    
while(True):
    check_price()
    #time.sleep(60 * 60) u can use this to re run script for more check python docs
   
