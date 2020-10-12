## Zombie-taal - regels 3 en 4

Regel 3 bepaalt dat kleine letters 'r' aan het einde van woorden moeten worden vervangen door 'rh'.

- Je hebt geleerd hoe je `\b` kunt gebruiken om patronen te zoeken aan het begin en einde van woorden.

[[[generic-python-regex-substitute-word-boundaries]]]

- Je moet nu een patroon construeren om naar `'r'` tekens aan het einde van een woord te zoeken en deze te vervangen door `'rh'`

- Om regel 4 te volgen, heb je een ander vervangingspatroon nodig dat op zoek is naar de tekens `'a'` en `'A'` als ze op zichzelf staan en deze vervangen door `'hra'`

--- hints ---
 --- hint ---

- Het eerste patroon waar je naar zoekt is `r'r\b'`.

--- /hint ---
--- hint ---

- Je volledige vervanging ziet er als volgt uit:

```python
tekst = re.sub(r'r\b', 'rh', tekst)
```

--- /hint --- --- hint ---

- Om losstaande `a` of `A` tekens te vinden, kun je het patroon `r'(\b[aA]\b)'` gebruiken.

```python
tekst = re.sub(r'(\b[aA]\b)','hra', tekst)
```

--- /hint ------ /hints ---
