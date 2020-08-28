## Los zombies gimen y gruñen

- Vamos a cambiar el texto en el que estás trabajando.
  ```python
  texto = '"Estoy cansado", dijo el hombre'
  ```

- Los zombies no dicen cosas, ellos gruñen, gimen y rugen. Por lo tanto, el texto necesita una mayor modificación.

- Empieza haciendo una lista de palabras que indican hablar. Aquí tienes unos ejemplos:

    ```python
    hablando = ['dijo', 'respondió', 'habló', 'gritó', 'lloró', 'susurró']
    ```

- Luego haz otra lista usando palabras que describan cómo suenan los zombies. Aquí hay algunas con las que te gustaría empezar:

    ```python
    sonidos_zombie = ['gruñó', 'gimió', 'rugió', 'chilló', 'gorgoteó']
    ```

- Ahora puedes usar otro bucle para reemplazar cada palabra del texto que esté en la lista `hablando` con una palabra aleatoria de la lista `sonidos_zombie`.

- Primero tendrás que importar el método `choice` del módulo `random`.

    ```python
    import re
    from random import choice
    ```

- Luego construye el bucle for, usando el mismo método de sustitución regex que usaste antes, pero esta vez usando un elemento aleatorio de `sonidos_zombie`.

    ```python
    for palabra in hablando:
        texto = re.sub(r'\b{0}\b'.format(palabra), choice(sonidos_zombie), texto)
    ```

- Ejecutar tu código ahora debería darte la siguiente salida, con la última palabra seleccionada aleatoriamente de la lista.

```python
>>> "Estoy cansado", el zombie gimió
```
