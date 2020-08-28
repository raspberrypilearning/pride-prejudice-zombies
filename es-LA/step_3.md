## Haciéndolo todo sobre zombies

- Primero vas a averiguar cómo cambiar una frase simple para que se trate de zombies.

    ```
    La mujer se rió de los hombres tontos.
    ```

- Para empezar, solo hay dos palabras que reemplazar: `'mujer'` y `'hombres'`. La primera debe convertirse en `'zombie'` y la segunda debe convertirse en `'zombies'`.

- Para reemplazar estas palabras, puedes usar **ex**presiones **re**gulares, o regex en inglés. Regex te permite encontrar **patrones** de caracteres en texto. Echa un vistazo a la sección de abajo, y mira si puedes averiguar cómo convertir la frase anterior para que se lea:

    ```
    El zombie se rió de los zombies tontos.
    ```

[[[generic-python-regex-substitute-simple-pattern]]]

--- hints --- --- hint ---

Comienza importando el módulo `re` y creando la cadena que quieres modificar.

```python
import re
text = 'La mujer se rió de los hombres tontos.'
```

--- /hint --- --- hint ---

Ahora quieres usar el método `re.sub()` para primero cambiar `'mujer'` a `'zombie'`, y luego usarlo de nuevo para cambiar `'hombres'` a `'zombies'`.

```python
text = re.sub('patrón a encontrar', 'patrón a reemplazar', texto)
```

--- /hint --- --- hint ---

Por lo tanto, tu primera sustitución se vería así.

```python
texto = re.sub('mujer', 'zombie', texto)
```

Ahora solo tienes que repetir esta línea pero usando `'hombres'` y `'zombies'`.

--- /hint --- --- /hints ---
