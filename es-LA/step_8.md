## Zombie Austen

- Hasta ahora has estado trabajando en unas pocas oraciones, pero el código que has escrito también funcionará en textos largos.

- Hay un gran número de libros en el dominio público. Están disponibles en el sitio web [Project Gutenberg](https://www.gutenberg.org/). Incluido en el archivo está el libro de Jane Austen [*Orgullo y prejuicio*](https://www.gutenberg.org/files/1342/1342-0.txt).

- Puedes usar Python para obtener este libro desde el sitio web, pero necesitarás usar el módulo `requests`. Importa el módulo junto con los otros módulos.

    ```python
    import re
    from random import choice
    import requests
    ```

- Ahora usa el módulo `requests` para obtener el libro en https://www.gutenberg.org/files/1342/1342-0.txt, y almacena su texto usando el nombre de variable `texto`.

- La siguiente sección muestra cómo obtener una página web y almacenarla. Sólo tendrás que ajustar la `url`.

[[[generic-python-requests]]]

- Una vez que tengas el texto, probablemente sea mejor escribir los datos en un archivo, en lugar de imprimirlo directamente en la pantalla.

[[[generic-python-writing-to-a-file]]]

--- hints --- --- hint ---

- Primero necesita obtener los datos de la página:

  ```python
  url = "https://www.gutenberg.org/files/1342/1342-0.txt"
  r = requests.get(url)
  ```

--- /hint --- --- hint ---

- El texto se puede extraer de los datos. Primero elimina la línea en la que has establecido `texto` a cualquier cadena con la que estabas experimentando. Luego reemplázalo con esto:

  ```python
  texto = r.text
  ```

--- /hint --- --- hint ---

- En lugar de imprimir el texto en la pantalla, deberías escribirlo en un archivo. Así que elimina las líneas `print(texto)` que tengas, y en su lugar usa esto al final de tu código:

  ```python
  with open('Zombies.txt', 'w', encoding="utf-8") as f:
      f.write(texto)
  ```

--- /hint --- --- /hints ---
