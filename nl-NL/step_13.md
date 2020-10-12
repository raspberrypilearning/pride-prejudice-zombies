## De vertaler samenstellen

- Je kunt nu alle vervangingen samenvoegen.

    ```python
    import re
    tekst = 'The quick brown fox jumped over the lazy dog'

    def zombificeer_spraak(tekst):
        tekst = re.sub(r'[eiosEIOS]', 'r', tekst)
        tekst = re.sub(r'[^zhrgbmnaZHRGBMNA?\n .!?-]', '', tekst)
        tekst = re.sub(r'r\b', 'rh', text)
        tekst = re.sub(r'(\b[aA]\b)','hra', text)
        return tekst

    tekst = zombificeer_spraak(tekst)
    ```

- Als je je programma uitvoert en vervolgens de waarde van `tekst` in de interpreter opvraagt, zou je het volgende moeten zien.

    ```python
    >>> tekst
    'hrh rh brrn rh mrh rrrh hrh az rg'
    ```
