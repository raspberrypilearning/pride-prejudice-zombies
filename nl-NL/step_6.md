## De zombies zijn er mee bezig

- Tot nu toe, afgezien van de lijsten met woorden die je hebt gegenereerd en de import, zou de basislogica van je script er ongeveer zo uit moeten zien:

    ```python
    for woord in meervoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'zombies', tekst)
    for woord in enkelvoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'zombie', tekst)
    ```

- Dit werkt prima voor de meeste teksten, maar in het volgende voorbeeld mislukt het:

```python
tekst = 'Ladies and Gentlemen, will the boys and girls please leave'
```

- Dit komt omdat onze regexvervangingen hoofdlettergevoelig zijn. Dus terwijl `ladies'` wordt gewijzigd in `'zombies'`, wordt `'Ladies'` niet gewijzigd.

- Het is mogelijk om hoofdletters te negeren bij een regex-zoekopdracht, maar dat zou alleen maar kleine letters maken, en zombies haten een slechte grammatica, dus het is niet de beste oplossing.

- In plaats daarvan kun je nieuwe lijsten maken met woorden die beginnen met hoofdletters en kleine letters met behulp van twee kleine trucs: **list comprehensions (lijstbegrippen)** en **case operations (kleine- en hoofdletteroperaties)**.

[[[generic-python-string-operations-case]]] 
[[[generic-python-simple-list-comprehensions]]]

- Je kunt **kleine- en hoofdletteroperaties** en **lijstbegrippen** toepassen om dit te gebruiken:
  ```python
  ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']
  ```

  om het volgende te maken:

  ```python
  ['Ladies', 'Gentlemen', 'Women', 'Men', 'Children', 'Boys', 'Girls']
  ```

- Gebruik wat je hebt geleerd om twee **nieuwe** lijsten te maken met de naam `meervoud_zelfstandig_naamwoorden_titel` en `enkelvoud_zelfstandig_naamwoorden_titel`.

--- hints ---
 --- hint ---

- `'ladies'` kan worden omgezet in `'Ladies'` met behulp van de bewerking `.title()`.

    ```python
    >>> 'ladies'.title()
    'Ladies'
    ```

--- /hint ---
--- hint ---

- De basisstructuur van het lijstbegrip zou ongeveer zo zijn:

    ```python
    [woord.title() for woord in meervoud_zelfstandig_naamwoord]
    ```

--- /hint --- 
--- hint ---

- Het volledige lijstbegrip zal zijn:
  ```python
  meervoud_zelfstandig_naamwoorden_titel = [woord.title() for woord in meervoud_zelfstandig_naamwoorden]
  ```

- Hetzelfde moet worden gedaan voor de enkelvoud zelfstandige naamwoorden.

--- /hint ------ /hints ---

- Nu heb je nog eens **twee** `for` lussen nodig. Een voor `meervoud_zelfstandig_naamwoorden_titel` en een voor `enkelvoud_zelfstandig_naamwoorden_titel`.

    ```python
    for woord in meervoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'Zombies', tekst)
    for woord in enkelvoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'Zombie', tekst)
    ```
