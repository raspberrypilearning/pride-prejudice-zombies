## Zombie-taal - regel 2

De tweede regel voor het converteren van Engels naar zombietaal is:

- Alle tekens behalve "zhrgbmna.!? -" (niet hoofdlettergevoelig) worden verwijderd.

Om dit te doen, kun je opnieuw naar meerdere karakters zoeken. Maar deze keer wil je bepaalde tekens uitsluiten van de regex-zoekopdracht.

[[[generic-python-regex-excluding-patterns]]]

- Gebruik de bovenstaande informatie om alle tekens te vervangen, behalve `zhrgbmna?\n .!?-` door een lege string (`""`).

--- hints ---
 --- hint ---

- Vergeet niet dat je hoofdletters en kleine letters moet uitsluiten.

  ```python
  zhrgbmnaZHRGBMNA“”?\n .!?-
  ```

--- /hint ---

--- hint ---

- Het patroon dat je wilt uitsluiten wordt daarom:

  ```python
  r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]'
  ```

--- /hint ---
--- hint ---

- Je volledige vervanging ziet er als volgt uit:

  ```python
  tekst = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', tekst)
  ```

--- /hint --- --- /hints ---
