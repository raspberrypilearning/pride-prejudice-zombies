import re
from random import choice
import requests

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
r = requests.get(url)
texto = r.text

def cambiar_prosa(texto):
    sustantivos_plurales = ['damas', 'caballeros', 'mujeres', 'hombres', 'hijos', 'niños', 'niñas']

    sustantivos_singulares = ['hijo', 'hija', 'niño', 'esposa', 'mujer', 'señora', 'señorita', 'esposo', 'hombre', 'señor', 'caballero', 'dama']

    hablando = ['dijo', 'respondió', 'habló', 'gritó', 'lloró']
    sonidos_zombie = ['gruñó', 'gimió', 'rugió', 'chilló', 'gorgoteó']

    sustantivos_plurales = sustantivos_plurales + [palabra.title() for palabra in sustantivos_plurales]
    sustantivos_singulares = sustantivos_singulares + [palabra.title() for palabra in sustantivos_singulares]

    for palabra in sustantivos_plurales:
        texto = re.sub(r'\b{0}\b'.format(palabra), 'zombies', texto)
    for palabra in sustantivos_singulares:
        texto = re.sub(r'\b{0}\b'.format(palabra), 'zombie', texto)
    for palabra in hablando:
        texto = re.sub(r'\b{0}\b'.format(palabra), choice(sonidos_zombie), texto)
    return(texto)

def zombificar_discurso(texto):
	texto = re.sub(r'[eiosEIOS]', 'r', texto)
	texto = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', texto)
	texto = re.sub(r'r\b', 'rh', texto)
	texto = re.sub(r'(\b[aA]\b)','hra', texto)
	return texto

discurso = re.findall(r'“.*?”', texto, flags=re.DOTALL)
for palabras in discurso:
    texto= texto.replace(palabras, zombificar_discurso(palabras))
texto = cambiar_prosa(texto)
with open('Zombie.txt', 'w') as f:
    f.write(texto)
