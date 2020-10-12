## Zombie Austen

- Tot nu toe heb je aan een paar zinnen gewerkt, maar de code die je hebt geschreven, werkt ook op grote teksten.

- Er zijn een groot aantal boeken in het publieke domein. Ze zijn beschikbaar op de [Project Gutenberg-website](https://www.gutenberg.org/). In het archief is opgenomen het boek [*Pride and Prejudice (Trots en vooroordeel)*](https://www.gutenberg.org/files/1342/1342-0.txt) van Jane Austen.

- Je kunt Python gebruiken om dit boek van de website te halen, maar je moet de module `requests` gebruiken. Importeer de module samen met je andere modules.

    ```python
    import re
    from random import choice
    import requests
    ```

- Gebruik nu de module `requests` om het boek op te halen op https://www.gutenberg.org/files/1342/1342-0.txt en sla de tekst op in de variabele met naam `tekst`.

- In het onderstaande gedeelte wordt uitgelegd hoe je een webpagina kunt ophalen en opslaan. Je hoeft alleen de `url` aan te passen.

[[[generic-python-requests]]]

- Zodra je de tekst hebt, is het waarschijnlijk het beste om de gegevens naar een bestand te schrijven in plaats van deze af te drukken.

[[[generic-python-writing-to-a-file]]]

--- hints ---
 --- hint ---

- Eerst moet je de paginagegevens ophalen:

  ```python
  url = "https://www.gutenberg.org/files/1342/1342-0.txt"
  r = requests.get(url)
  ```

--- /hint ---
--- hint ---

- De tekst kan vervolgens uit de gegevens worden gehaald. Verwijder eerst de regel waar je momenteel `tekst` instelt op de string waarmee je experimenteerde. Vervang het dan door dit:

  ```python
  tekst = r.text
  ```

--- /hint ---
---
hint ---

- In plaats van de tekst af te drukken, moet je deze naar een bestand schrijven. Verwijder dus alle `print(tekst)` regels die je hebt, en gebruik het volgende in plaats daarvan helemaal aan het einde van je script:

  ```python
  with open('Zombies.txt', 'w', encoding="utf-8") as f:
      f.write(tekst)
  ```

--- /hint --- --- /hints ---
