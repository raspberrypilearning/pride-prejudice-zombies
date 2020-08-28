## Idioma zombie - regla 2

La segunda regla para convertir el español al idioma zombie es:

- Todos los caracteres que no sean "zhrgbmna.!? -" (sin distinción entre mayúsculas y minúsculas) se eliminan.

Para hacer esto, puede buscar multiples caracteres de nuevo. Pero esta vez querrás excluir ciertos caracteres de la búsqueda regex.

[[[generic-python-regex-excluding-patterns]]]

- Usa la información anterior para reemplazar todos los caracteres excepto `zhrgbmna?\n .!?-` por una cadena vacía (`""`).

--- hints --- --- hint ---

- No olvides que necesitas excluir caracteres en mayúsculas y minúsculas.

  ```python
  zhrgbmnaZHRGBMNA“”?\n .!?-
  ```

--- /hint --- --- hint ---

- El patrón que deseas excluir se convierte en:

  ```python
  r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]'
  ```

--- /hint --- --- hint ---

- Tu sustitución completa se verá así:

  ```python
  texto = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', texto)
  ```

--- /hint --- --- /hints ---
