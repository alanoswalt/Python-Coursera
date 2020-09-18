from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Otra forma de sumar numeros por medio de 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =  ' http://py4e-data.dr-chuck.net/comments_716664.html'
html=urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, "html.parser")
suma=0
tags = soup('span')
numbers = list()
for tag in tags:
    number=int(tag.contents[0])
    numbers.append(number)
    suma=sum(numbers)
print(suma)
