## Los zombies están en las mayúsculas

- Hasta ahora, aparte de las listas de palabras que generaste y las importaciones, la lógica básica de tu código debería verse así:

    ```python
    for palabra in sustantivos_plurales:
        texto = re.sub(r'\b{0}\b'.format(palabra), 'zombies', texto)
    for palabra in sustantivos_singulares:
        texto = re.sub(r'\b{0}\b'.format(palabra), 'zombie', texto)
    ```

- Esto funciona bien para la mayoría de los textos, pero fallará en el siguiente ejemplo:

```python
text = 'Damas y Caballeros, los niños y niñas por favor salgan'
```

- Esto se debe a que nuestras sustituciones regex distinguen entre mayúsculas y minúsculas. Así que, mientras que `'damas'` se cambiará a `'zombies'`, `'Damas'` no se cambiará.

- Es posible ignorar mayúsculas y minúsculas en una búsqueda regex, pero eso convertiría todo a minúscula, y los zombies odian la mala gramática, por lo que no es la mejor solución.

- En su lugar, puedes crear nuevas listas que contengan palabras que empiecen con letras mayúsculas y minúsculas usando dos pequeños trucos: **comprensiones de lista** y **operaciones con mayúsculas y minúsculas**.

\[[[generic-python-string-operations-case]]\] \[[[generic-python-simple-list-comprehensions\]]]

- Puedes usar **operaciones con mayúsculas y minúsculas** y **comprensiones de lista** para usar esto:
  ```python
  ['damas', 'caballeros', 'mujeres', 'hombres', 'hijos', 'niños', 'niñas']
  ```

  y crear lo siguiente:

  ```python
  ['Damas', 'Caballeros', 'Mujeres', 'Hombres', 'Hijos', 'Niños', 'Niñas']
  ```

- Usa lo que has aprendido para crear dos listas **nuevas** llamadas `sustantivos_plurales_title` y `sustantivos_singulares_title`.

--- hints --- --- hint ---

- `'damas'` puede convertirse en `'Damas'` usando la operación `.title()`.

    ```python
    >>> 'damas'.title()
    'Damas'
    ```

--- /hint --- --- hint ---

- La estructura básica de la comprensión de lista sería algo así:

    ```python
    [palabra.title() for palabra in sustantivos_plurales]
    ```

--- /hint --- --- hint ---

- La comprensión de lista completa será:
  ```python
  sustantivos_plurales_title = [palabra.title() for palabra in sustantivos_plurales]
  ```

- Lo mismo debe hacerse para los sustantivos singulares.

--- /hint --- --- /hints ---

- Ahora necesitarás **dos** bucles `for` adicionales. Uno para `sustantivos_plurales_title` y otro para `sustantivos_singulares_title`.

    ```python
    for palabra in sustantivos_plurales_title:
        texto = re.sub(r'\b{0}\b'.format(palabra), 'Zombies', texto)
    for palabra in singular_nouns_title:
        texto = re.sub(r'\b{0}\b'.format(palabra), 'Zombie', texto)
    ```
