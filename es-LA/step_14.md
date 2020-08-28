## Encontrando discursos

- La siguiente etapa es encontrar todo el discurso en *Orgullo y prejuicio*, y hacerlo pasar por tu traductor.

- Para hacer esto, primero echemos un vistazo a algún discurso del libro.

```
"Mi querido señor Bennet", le dijo un día su esposa, "¿sabías que por fin se ha alquilado Netherfield Park?"
```

- Notará que el discurso está contenido entre comillas dobles. Sin embargo, estas no son las comillas normales que encuentras en el teclado de tu computadora. Mira de cerca y deberías ver que tanto `“` como `”` son diferentes de `"`.

- Una vez más, las expresiones regulares pueden utilizarse para encontrar todo el texto entre dos caracteres cualquiera.

[[[generic-python-regex-text-between-patterns]]]

- Ahora querrás buscar el texto en el libro y encontrar todas las cadenas rodeadas por `“` y `”`. Recuerda que no se trata de comillas dobles normales, así que necesitas copiarlas y pegarlas desde esta página. Almacena los resultados de tu búsqueda en una lista con el nombre `discurso`.

--- hints --- --- hint ---

Usa `re.findall` con un patrón que haga coincidir todo entre `“` y `”`.

--- /hint --- --- hint ---

No hay necesidad de usar los elementos de 'mirar adelante' o 'mirar atrás' en esta búsqueda, pero estás mirando cadenas de múltiples líneas, así que se necesitará la bandera `re.DOTALL`.

--- /hint --- --- hint ---

Tu búsqueda debería verse así:

```python
texto = "Mi querido señor Bennet", le dijo un día su esposa, "¿sabías que por fin se ha alquilado Netherfield Park?"
discurso = re.findall(r'“.*?”', texto, flags=re.DOTALL)
```

--- /hint --- --- /hints ---
