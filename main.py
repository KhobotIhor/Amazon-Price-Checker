import requests
import smtplib
from bs4 import BeautifulSoup
email_pass = 'ugwd fmin cjoc siph'
email = 'erkeblanharacuev@gmail.com'
url = 'https://www.amazon.com/OnePlus-Dual-SIM-Unlocked-Smartphone-Hasselblad/dp/B0CSCKTT7N/ref=sr_1_10?crid=LT0QS1IJEV5&dib=eyJ2IjoiMSJ9.IEMppGclo5bWdz_z-php-nFLgSeVSN3eqL5E-24CTybCz_PyVCZHv1ql71DzdMtzWag_1F4f-_a46quVhl52AO3nf1ZqtEIv5jgf8eaJzq5t_HGp2XQ6kdRA3ZQ7aoguefKHDtZidRsJlGF86Bnf56GVKrmpmLBl-vweZC08fwBIFy6VhHLO-VPLN7RHyAjG586mM0tq7wPLGJpbipzebUhB76EEgC9Hhkk9ciNIAhM.rB5aWLkXi1VKny4SURGUhE1N3YbS4skpCtAimCQunnk&dib_tag=se&keywords=iphone%2B15&qid=1709141048&sprefix=iphone%2B15%2Caps%2C231&sr=8-10&th=1'
acquisition_price = 1200

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

price = float(soup.find('span', class_='a-offscreen').getText().replace('$', '').replace(',', ''))
product_title = soup.find('span', id='productTitle').getText()
if price >= acquisition_price:
    connection = smtplib.SMTP(host='smtp.gmail.com')
    connection.starttls()
    connection.login(user=email, password=email_pass)
    connection.sendmail(from_addr=email, to_addrs='ihor.khobot@icloud.com', msg=f'Subject: Amazon Price Alert!\n\n{product_title} costs {price}$ now!\n{url}')


