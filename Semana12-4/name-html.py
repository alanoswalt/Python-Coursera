from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =  input('Enter URL ')
x=int(input('Enter number of links '))
y=int(input('Enter position '))
z=0

while(z<x):
    html=urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print(tags[y-1].contents[0])
    url=(tags[y-1].get('href', None))
    z=z+1
