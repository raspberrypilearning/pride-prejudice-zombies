## Functies toevoegen
- Je code zou er ongeveer als volgt uit moeten zien:

    ```python
    import re
    from random import choice
    import requests

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    r = requests.get(url)
    tekst = r.text

    meervoud_zelfstandig_naamwoorden = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']

    enkelvoud_zelfstandig_naamwoorden = ['son', 'daughter', 'child','wife', 'woman', 'mrs', 'miss','husband', 'man', 'mr', 'sir', 'lady']

    spreken = ['said', 'replied', 'spoke', 'shouted', 'cried']
    zombie_geluiden = ['groaned', 'moaned' ,'growled', 'screamed', 'gurgled']

    meervoud_zelfstandig_naamwoorden = meervoud_zelfstandig_naamwoorden + [woord.title() for woord in meervoud_zelfstandig_naamwoorden]
    enkelvoud_zelfstandig_naamwoorden = enkelvoud_zelfstandig_naamwoorden + [woord.title() for woord in enkelvoud_zelfstandig_naamwoorden]


    for woord in meervoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'zombies', tekst)
    for woord in enkelvoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'zombie', tekst)
    for word in spreken:
        tekst = re.sub(r'\b{0}\b'.format(woord), choice(zombie_geluiden), tekst)

    with open('Zombie.txt', 'w', encoding="utf-8") as f:
        f.write(tekst)
    ```

- Als je de code uitvoert en vervolgens in je map kijkt, zou je een nieuw bestand moeten zien met de naam **Zombie.txt**. Bekijk het bestand door het met een willekeurige teksteditor te openen.

- De eerste alinea van hoofdstuk 1 zou nu moeten luiden: **It is a truth universally acknowledged, that a single zombie in possession of a good fortune, must be in want of a zombie.**

- De eerste keer dat iemand in het boek spreekt, zou het er zoiets moeten uitzien als: **“My dear zombie. Bennet,” moaned his zombie to him one day, “have you heard that Netherfield Park is let at last?”**

- Vergelijk jouw code met de bovenstaande versie als deze niet werkt.

- Nu wil je je code een beetje opruimen voordat je naar het volgende deel gaat. Plaats de kerncode die de tekst omzet in een **functie** en roep deze vervolgens aan.

    ```python
    import re
    from random import choice
    import requests

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    r = requests.get(url)
    tekst = r.text

    def verander_proza(tekst):
        meervoud_zelfstandig_naamwoorden = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']

        enkelvoud_zelfstandig_naamwoorden = ['son', 'daughter', 'child','wife', 'woman', 'mrs', 'miss','husband', 'man', 'mr', 'sir', 'lady']

        spreken = ['said', 'replied', 'spoke', 'shouted', 'cried']
        zombie_geluiden = ['groaned', 'moaned' ,'growled', 'screamed', 'gurgled']

        meervoud_zelfstandig_naamwoorden = meervoud_zelfstandig_naamwoorden + [word.title() for word in meervoud_zelfstandig_naamwoorden]
        enkelvoud_zelfstandig_naamwoorden = enkelvoud_zelfstandig_naamwoorden + [word.title() for word in enkelvoud_zelfstandig_naamwoorden]


        for word in meervoud_zelfstandig_naamwoorden:
            tekst = re.sub(r'\b{0}\b'.format(word), 'zombies', tekst)
        for word in enkelvoud_zelfstandig_naamwoorden:
            tekst = re.sub(r'\b{0}\b'.format(word), 'zombie', tekst)
        for word in spreken:
            tekst = re.sub(r'\b{0}\b'.format(word), choice(zombie_geluiden), tekst)
        return(text)

    tekst = verander_proza(tekst)

    with open('Zombie.txt', 'w', encoding="utf-8") as f:
        f.write(tekst)
    ```
