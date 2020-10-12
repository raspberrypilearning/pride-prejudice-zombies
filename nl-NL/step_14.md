## Spraak zoeken

- De volgende fase is om alle spraak in *Pride en Prejudice* te vinden en door je vertaler te laten lopen.

- Laten we eerst wat spraak uit het boek bekijken.

```
“My dear Mr. Bennet,” said his lady to him one day, “have you heard that Netherfield Park is let at last?”
```

- Je zult merken dat de spraak tussen dubbele aanhalingstekens staat. Dit zijn echter niet de normale aanhalingstekens die je op jouw computertoetsenbord vindt. Kijk goed en je zou moeten zien dat zowel `"` als `"` verschillen van `"`.

- Nogmaals, reguliere expressies kunnen worden gebruikt om alle tekst tussen twee willekeurige tekens te vinden.

[[[generic-python-regex-text-between-patterns]]]

- Nu wil je de tekst in het boek doorzoeken en alle tekenreeksen vinden tussen `"` en `"` vinden. Vergeet niet dat dit geen normale dubbele aanhalingstekens zijn, dus je moet ze kopiëren en plakken vanaf deze pagina. Bewaar de resultaten van je zoekopdracht in een lijst met de naam `spraak`.

--- hints ---
 --- hint ---

Gebruik `re.findall` met een patroon dat overeenkomt met alles tussen `“` and `”`.

--- /hint --- --- hint ---

Het is niet nodig om de 'look ahead' (kijk vooruit) of 'look behind' (kijk achteruit)-elementen te gebruiken in deze zoekopdracht, maar je kijkt naar strings over meerdere regels, dus de `re.DOTALL` vlag is nodig.

--- /hint --- --- hint ---

Je code zou er als volgt uit moeten zien:

```python
tekst = “My dear Mr. Bennet,” said his lady to him one day, “have you heard that Netherfield Park is let at last?”
spraak = re.findall(r'“.*?”', tekst, flags=re.DOTALL)
```

--- /hint ------ /hints ---
