## Overal zombies

- Er is een probleem met je script zoals het nu is. Overweeg deze zin:

    ```
    tekst = "The men of the establishment were managing to manoeuvre the mentors."
    ```

- Wijzig de tekst in je script in de hierboven genoemde tekst en voer deze opnieuw uit. Deze keer ziet je tekst er een beetje vreemd uit.

    ```
    The zombies of the establishzombiest were zombieaging to zombieoeuvre the zombiestors.
    ```

- Dat zijn veel te veel zombies! Elk `'man'` of `'men'` patroon in de tekst is veranderd in `'zombie'`, dus het woord `'mentors'` is nu `'zombiestors'`. Hoe kan dit worden opgelost?

- Gelukkig hebben de slimme mensen die met Regex kwamen hierover nagedacht, en er is een manier om alleen hele woorden te matchen.

[[[generic-python-regex-substitute-word-boundaries]]]

- Als je `r'\bman\b'` als je zoekpatroon gebruikt, wordt alleen het specifieke woord `man` gevonden. Je zou dan `re.sub()` kunnen gebruiken om `man` te ruilen voor `zombie`. Dit zou echter betekenen dat veel lussen worden gebruikt; één voor elke vervanging. Door de methode `.format` in Python te gebruiken, kun je ervoor zorgen dat je slechts twee lussen gebruikt; één voor meervoud zelfstandige naamwoorden en één voor enkelvoud zelfstandige naamwoorden.

[[[generic-python-simple-string-formating]]]

- Probeer nu `.format()` in jouw `re.sub ()` methoden, om automatisch `'ladies'` in `'zombies'` en `'gentlemen'` in `'zombies'` te veranderen. Je kunt het op dit stukje tekst uitproberen:

```python
tekst = "The gentlemen of the establishment were managing to manoeuvre the mentors, while the ladies relaxed and watched in amusement"
```

--- hints --- --- hint ---

- Hier zie je hoe je het patroon kunt instellen waarnaar je op zoek bent.

```python
r'\b{0}\b'.format(woord)
```

--- /hint hint ---

- Binnen een van je for-loops zou het er zo uitzien:

```python
for woord in meervoud_zelfstandig_naamwoord:
    tekst = re.sub(r'\b{0}\b'.format(woord), 'zombies', tekst)
```

- Nu zou je in staat moeten zijn om de tweede for lus zelf te doen.

--- /hint --- --- /hints ---
