## Añadiendo funciones
- Tu código debería verse algo así:

    ```python
    import re
    from random import choice
    import requests

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    r = requests.get(url)
    texto = r.text

    sustantivos_plurales = ['damas', 'caballeros', 'mujeres', 'hombres', 'hijos', 'niños', 'niñas']

    sustantivos_singulares = ['hijo', 'hija', 'niño', 'esposa', 'mujer', 'señora', 'señorita', 'esposo', 'hombre', 'señor', 'caballero', 'dama']

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

    with open('Zombie.txt', 'w', encoding="utf-8") as f:
        f.write(texto)
    ```

- Si ejecutas el código y buscas en tu directorio, deberías ver un nuevo archivo creado llamado **Zombie.txt**. Echa un vistazo al archivo abriéndolo con cualquier editor de texto.

- El primer párrafo del Capítulo 1 debe ahora decir: **Es una verdad mundialmente reconocida que un zombie soltero en posesión de una gran fortuna, necesita una zombie.**

- La primera vez que alguien en el libro habla, debería decir algo como: **"Mi querido zombie. Bennet", le gimió un día su zombie, "¿sabías que por fin se ha alquilado Netherfield Park?"**

- Compara tu código con la versión mostrada arriba si es que no funciona.

- Ahora querrás ordenar tu código un poco antes de pasar a la siguiente parte. Coloca el código principal que convierte el texto en una **función** y luego llámalo.

    ```python
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

    texto = cambiar_prosa(texto)

    with open('Zombie.txt', 'w', encoding="utf-8") as f:
        f.write(texto)
    ```
