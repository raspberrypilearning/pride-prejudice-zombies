from random import choice
import re

libro = open('oyp.txt','r')
texto = libro.read()

def encontrar_discurso(palabras):
    discurso = re.findall(r'“.*?”',palabras, flags=re.DOTALL)
    #discurso = re.findall(r'(?=“)(.*?)(?<=”)',palabras, flags=re.DOTALL)
    return discurso

def reemplazar_eios(palabras):
    '''todas las apariciones de los caracteres 'eiou' (mayúsculas y minúsculas) se reemplazan por "r".'''
    palabras = re.sub(r'[eiosEIOS]', 'r', palabras)
    return palabras

def eliminar_caracteres(palabras):
    '''todos los caracteres que no sean "zhrgbmna .!?-" (mayúsculas y minúsculas) se eliminan.'''
    palabras = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', palabras)
    return palabras

def reemplazar_r_final(palabras):
    '''una "r" minúscula al final de una palabra se reemplaza por "rh".'''
    palabras = re.sub(r'r\b', 'rh', palabras)
    return palabras

def reemplazar_a(palabras):
    '''una "a" or "A" por sí misma se reemplazará por "hra".'''
    palabras = re.sub(r'(\b[aA]\b)','hra',palabras)
    return palabras

def zombificar_discurso(palabras):
    palabras = reemplazar_eios(palabras)
    palabras = eliminar_caracteres(palabras)
    palabras = reemplazar_r_final(palabras)
    palabras = reemplazar_a(palabras)
    return palabras

def zombificar_prosa(palabras):
    sustantivos_singulares = ['Hijo', 'Hija', 'Niño', 'Esposa', 'Mujer', 'Señora', 'Señorita', 'Esposo', 'Hombre', 'Señor', 'Caballero', 'Dama']
    sustantivos_plurales = ['Damas', 'Caballeros', 'Mujeres', 'Hombres', 'Hijos', 'Niños', 'Niñas']
    discurso = ['Dijo', 'Respondió', 'Habló', 'Gritó', 'Lloró']
    for palabra in sustantivos_singulares:
        palabras = re.sub(r'\b{0}\b'.format(palabra), 'Zombie', palabras)
        palabras = re.sub(r'\b{0}\b'.format(palabra.lower), 'zombie', palabras)

    for palabra in sustantivos_plurales:
        palabras = re.sub(r'\b{0}\b'.format(palabra), 'Zombies', palabras)
        palabras = re.sub(r'\b{0}\b'.format(palabra.lower()), 'zombies', palabras)

    for palabra in discurso:
        palabras = re.sub(palabra, choice(['gruñó', 'gimió', 'resopló', 'rugió']), palabras)
    return palabras

for discurso in encontrar_discurso(texto):
    texto = texto.replace(discurso, zombificar_discurso(discurso))

texto = zombificar_prosa(texto)

with open('Version_Zombies.txt', 'w') as file:
    file.write(texto)
