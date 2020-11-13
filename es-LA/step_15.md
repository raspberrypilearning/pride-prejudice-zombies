## Terminando el libro para zombies

- Ahora tienes que unir todo: tu función para cambiar la prosa, tu función para traducir discursos y tu búsqueda de discursos.

- Tu archivo debería verse algo así:

    ```python
    import re
    from random import choice
    import requests

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    r = requests.get(url)
    texto = r.text

    def cambiar_prosa(texto):
        sustantivos_plurales = ['damas', 'caballeros', 'mujeres', 'hombres', 'hijos', 'niños', 'niñas']

        sustantivos_singulares = ['hijo', 'hija', 'niño','esposa', 'mujer', 'señora', 'señorita','esposo', 'hombre', 'señor', 'caballero', 'dama']

        hablando = ['dijo', 'respondió', 'habló', 'gritó', 'lloró']
        sonidos_zombie = ['gruñó', 'gimió' ,'rugió', 'chilló', 'gorgoteó']

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

    texto = cambiar_prosa(texto)

    discurso = re.findall(r'“.*?”', texto, flags=re.DOTALL)

    with open('Zombie.txt', 'w', encoding="utf-8") as f:
        f.write(texto)
    ```

- El último paso es ejecutarlo en todo el discurso del libro y traducirlo al lenguaje zombie. Esto puede ir justo antes de llamar a la función `cambiar_prosa()`.

```python
for palabras in discurso:
    texto = texto.replace(palabras, zombificar_discurso(palabras))
```

- Ahora ejecuta tu código y echa un vistazo a la versión zombie de _Orgullo y Prejuicio_ que ahora debería guardarse.

