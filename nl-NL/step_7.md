## Zombies kreunen en steunen

- Laten we de tekst wijzigen waaraan je werkt.
  ```python
  tekst = '"I am tired", the man said'
  ```

- Zombies zeggen geen dingen, ze kreunen, steunen en grommen. Dus de tekst moet verder worden aangepast.

- Begin met het maken van een lijst met woorden die op spraak wijzen. Hier zijn een paar voorbeelden:

    ```python
    spreken = ['said', 'replied', 'spoke', 'shouted', 'cried', 'whispered']
    ```

- Maak vervolgens een andere lijst met woorden die beschrijven hoe zombies klinken. Hier zijn een paar waarmee je misschien wilt beginnen:

    ```python
    zombie_sounds = ['groaned', 'moaned', 'growled', 'screamed', 'gurgled']
    ```

- Nu kun je een andere for-lus gebruiken om elk woord in de tekst in de `spreken` lijst te vervangen door een willekeurig woord uit de `zombie_geluiden` lijst.

- Eerst moet je de `choice` methode importeren uit de `random` module.

    ```python
    import re
    from random import choice
    ```

- Stel vervolgens de for-lus samen met dezelfde regex-substitutiemethode die je eerder hebt gebruikt, maar deze keer met een willekeurig item uit `zombie_geluiden`.

    ```python
    for woord in spreken:
        tekst = re.sub(r'\b{0}\b'.format(woord), choice(zombie_geluiden), tekst)
    ```

- Als je je code nu uitvoert, krijg je de volgende uitvoer, waarbij het laatste woord willekeurig wordt gekozen uit de lijst.

```python
>>> "I am tired", the zombie groaned
```
