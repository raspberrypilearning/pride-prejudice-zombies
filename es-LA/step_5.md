## Zombies en todas partes

- Hay un problema con tu código tal como está ahora. Considera esta oración:

    ```
    texto = "El hombre mandó a arreglar las hombreras de su traje para asistir a la fiesta del monseñor."
    ```

- Cambia el texto de tu código al texto de arriba y ejecútalo de nuevo. Esta vez se verá un poco extraño.

    ```
    El zombie mandó a arreglar las zombieras de su traje para asistir a la fiesta del monzombie.
    ```

- ¡Hay demasiados zombies! Cualquier patrón `'hombre'` o `'señor'` dentro del texto ha sido cambiado a `'zombie'`, por ejemplo la palabra `'hombreras'` ahora es `'zombieras'`. ¿Cómo se puede resolver esto?

- Por suerte, la gente inteligente que inventó regex pensó en esto, y hay una manera de hacer coincidir sólo palabras enteras.

[[[generic-python-regex-substitute-word-boundaries]]]

- Usando `r'\bhombre\b'` como patrón de búsqueda, sólo encontrarías la palabra específica `hombre`. Entonces podrías usar `re.sub()` para intercambiar `hombre` por `zombie`. Sin embargo, esto significaría usar muchos bucles; uno para cada sustitución. Usar el método `.format` en Python puede asegurarte que solo uses dos bucles; uno para sustantivos plurales y otro para sustantivos singulares.

[[[generic-python-simple-string-formating]]]

- Ahora intenta usar `.format()` dentro de tus métodos `re.sub()`, para convertir automáticamente `'damas'` en `'zombies'` y `'caballeros'` en `'zombies'`. Puedes probarlo en este fragmento de texto:

```python
texto = "El hombre mandó a arreglar las hombreras de su traje para asistir a la fiesta del monseñor. Al evento acudirían distinguidos caballeros y damas."
```

--- hints --- --- hint ---

- Así es como puedes configurar el patrón buscado.

```python
r'\b{0}\b'.format(palabra)
```

--- /hint --- --- hint ---

- Dentro de uno de tus bucles for, se vería así:

```python
for palabra in sustantivos_plurales:
    texto = re.sub(r'\b{0}\b'.format(palabra), 'zombies', texto)
```

- Ahora deberías poder hacer el segundo bucle for por ti mismo.

--- /hint --- --- /hints ---
