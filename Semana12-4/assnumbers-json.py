#DICT {} / LIST[] / TUPLES ()
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

#Con un documento JSON leerlo y tomar los numeros para sumarlos
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x=list()

while True:
    address = input('Enter location: ')
    uh = urllib.request.urlopen(address, context=ctx) #Abrir la puerta al texto
    data = uh.read().decode() #Leer informacion y decodificar porque esta en UTF-8
    print('Retrieved', len(data), 'characters')
    js=json.loads(data)
    #print(json.dumps(js,indent=4))

    for u in js['comments']:
        x.append(int(u['count']))
    print(sum(x))
