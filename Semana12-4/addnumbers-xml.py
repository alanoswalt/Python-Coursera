import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Usando xml sumar numeros agregandolos con una lista y sumando el contenidos
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x=list()


address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

comments = tree.findall('comments/comment/count')
print('Comments: ',len(comments))
for comment in comments:
    x.append(int(comment.text))
    #print(comment.find('name').text)
    #print(comment.text)
print(sum(x))
