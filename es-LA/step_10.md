## Idioma zombie

Aunque ahora se ha cambiado toda la prosa para que el libro sea más apropiado para los zombies, todo el discurso dentro del libro está todavía en español.

Aunque los zombies entienden el español, esa no es su forma de hablar. No es muy conocido, pero en realidad hay algunas reglas estrictas sobre cómo el español se traduce al idioma zombie:

1. Todas las apariciones de los caracteres 'eiou' (sin distinción entre mayúsculas y minúsculas) deben reemplazarse por 'r'
1. Todos los caracteres que no sean "zhrgbmna.!? -" (sin distinción entre mayúsculas y minúsculas) se eliminan
1. Cualquier 'r' en minúscula al final de una palabra se sustituye por 'rh'
1. Una 'a' o 'A' por sí misma tiene que ser reemplazada por 'hra'

- Una vez más, regex puede ayudarnos con esta tarea. En lugar de probarlo en todo el libro de inmediato, **crea un nuevo archivo Python**, para que puedas practicar en unas pocas frases de ejemplo.

# Regla 1

- Intenta convertir el siguiente texto usando la primera regla.

    ```python
    import re
    text = 'El veloz zorro marrón saltó sobre el perro perezoso'
    ```

- Echa un vistazo a la sección de abajo para aprender a sustituir múltiples caracteres diferentes con regex.

[[[generic-python-regex-substitute-multiple-characters]]]

- Ahora usa regex para completar la regla 1.

--- hints ---
 --- hint ---

- Necesitas convertir todos los caracteres `'e'`,`'i'`,`'o'`, and `'s'`, ya sean mayúsculas o minúsculas, en caracteres `'r'`.

--- /hint --- --- hint ---

- El patrón de regex que debes buscar es `[eiosEIOS]`.

--- /hint --- --- hint ---

- El texto se puede convertir con una sola línea:

    ```python
    texto = re.sub(r'[eiosEIOS]', 'r', texto)
    ```

--- /hint ------ /hints ---
