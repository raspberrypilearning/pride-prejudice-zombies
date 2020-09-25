## Múltiples reemplazos similares

- ¿Qué tal un pasaje de texto más complicado? Por ejemplo:

    ```python
    texto = "Los niños y niñas se rieron de la broma de la mujer. Al hombre no le pareció tan divertido."
    ```

- Crea un nuevo archivo Python y usa `import re` otra vez. Luego crea la cadena `texto` de arriba.

- Ahora hay dos grupos de sustantivos que necesitan ser reemplazados: sustantivos singulares como `mujer` y `hombre`, y sustantivos plurales como `niños` y `niñas`.

- ¿Cómo se podría "zombificar" este texto sin usar demasiadas líneas de código?

- Primero abordemos los sustantivos plurales. Si estuvieran en una **lista**, entonces podrías usar un bucle for para reemplazar cada una de las palabras de la lista.

[[[generic-python-for-loop-list]]]

- Crea una lista de sustantivos plurales que te gustaría cambiar a la palabra `zombies`.

    ```python
    sustantivos_plurales = ['damas', 'caballeros', 'mujeres', 'hombres', 'hijos', 'niños', 'niñas']
    ```

- Ahora necesitas iterar sobre la lista y usar `re.sub()` en cada palabra.

    ```python
    for palabra in sustantivos_plurales:
        texto = re.sub(palabra, 'zombies', texto)
    print(texto)
    ```

- Deberías ver la siguiente impresión:

    ```
    Los zombies y zombies se rieron de la broma de la mujer. Al hombre no le pareció tan divertido.
    ```

- Ahora intenta escribir otro bucle for para iterar sobre una lista de sustantivos singulares y reemplazarlos con `'zombie'`. Aquí hay una lista para que empieces:

    ```python
    sustantivos_singulares = ['hijo', 'hija', 'niño', 'esposa', 'mujer', 'señora', 'señorita', 'esposo', 'hombre', 'señor', 'caballero', 'dama']
    ```

--- hints ---
 --- hint ---

- Tu segundo bucle for debe comenzar debajo del primero, pero fuera de él.

--- /hint --- --- hint ---

- Aquí hay un código para comenzar:

```python
for palabra in sustantivos_plurales:
        texto = re.sub(palabra, 'zombies', texto)
for palabra en sustantivos_singulares:
```

--- /hint --- --- hint ---

- Usa `re.sub(palabra, 'zombie', texto)` para convertir las palabras en el texto.

--- /hint ------ /hints ---
