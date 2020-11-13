import requests
import re
from random import choice

#libro = requests.get("https://www.gutenberg.org/files/1342/1342-0.txt")
libro_texto = libro.text

resultado = re.findall('(?<=Capítulo 3)(.*?)(?=Capítulo 4)', libro_texto, flags=re.S)

capitulo_1 = resultado[0]

discurso = re.findall('(?<=“)(.*?)(?=”)', capitulo_1, flags=re.S)

## Reglas del idioma zombie
'''
- todas las apariciones de los caracteres 'eiou' (sin distinción entre mayúsculas y minúsculas) son reemplazadas por "r".
- todos los caracteres que no sean "zhrgbmna.!? -" (sin distinción entre mayúsculas y minúsculas) se eliminan.
- múltiples espacios se reemplazan con uno solo.
- 'r' minúscula al final de las palabras se sustituye por 'rh".
- una 'a' o 'A' por sí misma será reemplazada por 'hra".
- el inicio de las oraciones se escribe con mayúscula (el "comienzo de una oración" es cualquier aparición de ".!?", seguido de un espacio, seguido de una letra.)
- los espacios que preceden a cualquier ".!?" son eliminados.
- el primer caracter está en mayúscula.
'''
traductor = {palabras:palabras for palabras in discurso}

def reemplazar_eios(palabras):
    for caracter in 'eiosEIOS':
        palabras = palabras.replace(caracter, 'r')
    return palabras

def eliminar_caracteres(palabras):
    for caracter in palabras:
        if caracter.lower() not in 'zhrgbmna .!?-':
            palabras = palabras.replace(caracter, '')
    return palabras

def reemplazar_a(palabras):
    fin_de_palabra = '.,!?;: '
    for caracter in fin_de_palabra:
        palabras = palabras.replace(' a'+caracter, ' hra ')
        palabras = palabras.replace(' A'+caracter, ' hra')
    return palabras

for palabras in traductor.keys():
    traductor[palabras] = reemplazar_a(traductor[palabras])
    traductor[palabras] = reemplazar_eios(traductor[palabras])
    traductor[palabras] = eliminar_caracteres(traductor[palabras])

for palabras in traductor.keys():
    if palabras in capitulo_1:
        capitulo_1 = capitulo_1.replace(palabras, traductor[palabras])

sustantivos_singulares = [' Hijo ', ' Hija ', ' Niño ',' Esposa ', ' Mujer ', ' Señora ', ' Señorita ',' Esposo ', ' Hombre ', ' Señor ', ' Caballero ', ' Dama ']
sustantivos_plurales = [' Damas ', ' Caballeros', ' Mujeres ', ' Hombres ', ' Hijos ', ' Niños ', ' Niñas ']
hablando = ['dijo', 'respondió', 'habló', 'gritó', 'lloró']

for palabra in sustantivos_singulares:
    capitulo_1 = capitulo_1.replace(palabra, 'Zombie')
    capitulo_1 = capitulo_1.replace(palabra.lower(), 'zombie')

for palabra in sustantivos_plurales:
    capitulo_1 = capitulo_1.replace(palabra, 'Zombies')
    capitulo_1 = capitulo_1.replace(palabra.lower(), 'zombies')

for palabra in hablando:
    capitulo_1 = capitulo_1.replace(palabra, choice(['gruñó', 'gimió', 'resopló', 'rugió']))

with open('capitulo_1.txt', 'w') as f:
    f.write(capitulo_1)
