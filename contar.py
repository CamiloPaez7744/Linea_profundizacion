import sys
import collections

contador = 0
text = [' ']

#stdin = leer entrada
for linea in sys.stdin:
    contador = contador+1
    #strip = copia de informacion de la variable linea
    linea = linea.strip()
    #split = obtiene una lista 
    texto = linea.split()
    #if en python termina en :
    if(contador >=1):
        text = text +texto
#print(text)
#Se separó el texto en palábras
#print('Cantidad de líneas = ', contador )

#luego se ordenan las palabras del texto para 
text.sort(reverse= True)
#print(text)
#agrupar las palabras repetidas

contar = collections.Counter(text)
print(contar.most_common(10))

