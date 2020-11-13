## Idioma zombie - reglas 3 y 4

La regla 3 establece que los caracteres 'r' en minúscula al final de las palabras deben reemplazarse con 'rh'.

- Has aprendido a usar `\b` para buscar patrones al principio y al final de las palabras.

[[[generic-python-regex-substitute-word-boundaries]]]

- Ahora necesitas construir un patrón para buscar caracteres `'r'` al final de una palabra, y reemplazarlos por `'rh'`

- Para seguir la regla 4, necesitarás otro patrón de reemplazo que busque los caracteres `'a'` y `'A'` cuando estén solos, y los sustituya por `'hra'`

--- hints ---
 --- hint ---

- El primer patrón que estás buscando es `r'r\b'`.

--- /hint --- --- hint ---

- Tu sustitución completa se verá así:

```python
texto = re.sub(r'r\b', 'rh', texto)
```

--- /hint --- --- hint ---

- Para encontrar caracteres `a` o `A` solos, puedes usar el patrón `r'(\b[aA]\b)'`.

```python
texto = re.sub(r'(\b[aA]\b)','hra', texto)
```

--- /hint ------ /hints ---
