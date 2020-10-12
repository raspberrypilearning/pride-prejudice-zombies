## Meerdere vergelijkbare vervangingen

- Hoe zit het met een ingewikkeldere tekstpassage? Bijvoorbeeld:

    ```python
    tekst = "The boys and girls laughed at the woman's joke. The man did not find it so funny."
    ```

- Maak een nieuw Python bestand en `import re` weer. Maak vervolgens de tekenreeks `tekst` hierboven.

- Er zijn nu twee groepen zelfstandige naamwoorden die moeten worden vervangen: zelfstandige naamwoorden in het enkelvoud zoals `woman` en `man`, en zelfstandige naamwoorden in het meervoud zoals `boys` en `girls`.

- Hoe kan deze tekst gemakkelijk "gezombificeerd" worden zonder teveel regels code te gebruiken?

- Laten we eerst de zelfstandige naamwoorden in het meervoud aanpakken. Als ze in een **lijst** zitten, kun je een for-lus gebruiken om elk van de woorden in de lijst te vervangen.

[[[generic-python-for-loop-list]]]

- Maak een lijst met meerdere zelfstandige naamwoorden die je wilt wijzigen in het woord `zombies`.

    ```python
    meervoud_zelfstandig_naamwoord = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']
    ```

- Nu moet je de lijst herhalen en `re.sub ()` gebruiken voor elk woord.

    ```python
    for woord in meervoud_zelfstandig_naamwoorden:
        tekst = re.sub(woord, 'zombies', tekst)
    print(tekst)
    ```

- Je zou het volgende moeten zien:

    ```
    The zombies and zombies laughed at the woman's joke. The man did not find it so funny.
    ```

- Probeer nu een andere for-lus te schrijven die over een lijst met zelfstandige naamwoorden in het enkelvoud herhaalt en deze vervangt door `'zombie'`. Hier is een lijst om mee te beginnen:

    ```python
    enkelvoud_zelfstandig_naamwoorden = ['son', 'daughter', 'child', 'wife', 'woman', 'mrs', 'miss', 'husband', 'man', 'mr', 'sir', 'lady']
    ```

--- hints --- --- hint ---

- Je tweede for-lus zou onder de eerste moeten beginnen, maar daarbuiten.

--- /hint hint ---

- Hier is de code om mee te beginnen:

```python
for woord in meervoud_zelfstandig_naamwoorden:
  tekst = re.sub(woord, 'zombies', tekst)
for woord in enkelvoud_zelfstandig_naamwoorden:
```

--- /hint hint ---

- Gebruik `re.sub(woord, 'zombie', tekst)` om de woorden om te zetten in de tekst.

--- /hint --- --- /hints ---
