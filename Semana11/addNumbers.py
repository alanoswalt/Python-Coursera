import re

#Codigo donde se suma numeros
hand=open('regex_sum_716662.txt') #Abrir el archivo
print(hand)
numlist=list() #Crear una lista
for line in hand: # Por cada linea en lista
    x=line.split() #Hacer split al string conseguido
    if re.search('[0-9]', line): #buscar si la linea tiene un numero
        numbers=re.findall('[0-9]+',line) #Si la linea tiene un numero, buscar el componente con numero
#Numbres es una lista con todos los numeros, se convierten a int y se agregan a la nueva lista, al final se suma
        for number in numbers:
            n=int(number)
            numlist.append(n)
print(sum(numlist))
