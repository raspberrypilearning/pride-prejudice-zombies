## Alles over zombies maken

- Eerst ga je uitzoeken hoe je een eenvoudige zin kunt veranderen, zodat het allemaal over zombies gaat.

    ```
    The woman laughed at the silly men.
    ```

- Om te beginnen zijn er slechts twee woorden te vervangen: `'woman'` en `'men'`. De eerste moet `'zombie'` worden en de tweede moet `'zombies'` worden.

- Om deze woorden te vervangen, kun je **reg**ular **ex**pressions of regex gebruiken. Met regex kun je **patronen** van tekens in tekst vinden. Neem een kijkje in de onderstaande sectie en kijk of je kunt achterhalen hoe je de bovenstaande zin kunt converteren zodat deze luidt:

    ```
    The zombie laughed at the silly zombies.
    ```

[[[generic-python-regex-substitute-simple-pattern]]]

--- hints --- --- hint ---

Begin met het importeren van de `re` module en creëer de string die je wilt wijzigen.

```python
import re
tekst = 'The woman laughed at the silly men.'
```

--- /hint --- --- hint ---

Nu wil je de `re.sub()` methode gebruiken om eerst `'woman'` in `'zombie'` te veranderen en dan het nog een keer gebruiken om `'men'` in `'zombies'` te veranderen.

```python
tekst = re.sub('patroon om te vinden', 'patroon om te vervangen', tekst)
```

--- /hint --- --- hint ---

Je eerste wijziging zou er zo uit moeten zien.

```python
tekst = re.sub('woman', 'zombie', tekst)
```

Nu moet je dit herhalen maar dan gebruik je `'men'` en `'zombies'`.

--- /hint --- --- /hints ---
