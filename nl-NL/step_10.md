## Zombietaal

Hoewel al het proza is gewijzigd om het boek geschikter te maken voor zombies, is alle spraak in het boek nog steeds in gewoon Engels.

Hoewel zombies Engels kunnen begrijpen, is dat niet de manier waarop ze spreken. Het is niet bekend, maar er zijn eigenlijk enkele strikte regels met betrekking tot de vertaling van Engels in zombietaal:

1. Alle voorkomens van de tekens 'eiou' (niet hoofdlettergevoelig) moeten worden vervangen door 'r'
1. Alle tekens behalve 'zhrgbmna.!? -' (niet hoofdlettergevoelig) worden verwijderd
1. Elke kleine letter 'r' aan het einde van een woord wordt vervangen door 'rh'
1. Een 'a' of 'A' moet op zichzelf worden vervangen door 'hra'

- Opnieuw kan regex ons helpen met deze taak. In plaats van dit meteen in het hele boek uit te proberen, maak je **een nieuw Python-bestand**, zodat je op een paar voorbeeldzinnen kunt oefenen.

# Regel 1

- Probeer en converteer de volgende tekst met behulp van de eerste regel.

    ```python
    import re
    tekst = 'The quick brown fox jumped over the lazy dog'
    ```

- Neem een kijkje in de onderstaande sectie voor meer informatie over het vervangen van meerdere verschillende tekens door regex.

[[[generic-python-regex-substitute-multiple-characters]]]

- Gebruik nu regex om regel 1 te voltooien.

--- hints ---
 --- hint ---

- Je moet alle `'e'`,`'i'`,`'o'` en `'s'` tekens, zowel hoofdletters als kleine letters, vervangen door `'r'` tekens.

--- /hint --- --- hint ---

- Het regex patroon waar je naar zoekt is `[eiosEIOS]`.

--- /hint --- --- hint ---

- De tekst kan in een enkele regel code worden geconverteerd:

    ```python
    tekst = re.sub(r'[eiosEIOS]', 'r', tekst)
    ```

--- /hint ------ /hints ---
