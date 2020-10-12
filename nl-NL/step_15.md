## Het zombievriendelijke boek afmaken

- Je moet nu alles meenemen: jouw functie voor het wijzigen van het proza, jouw functie voor het vertalen van spraak en jouw zoektocht naar spraak.

- Je bestand zou er ongeveer zo uit moeten zien:

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

    meervoud_zelfstandig_naamwoorden = meervoud_zelfstandig_naamwoorden + [woord.title() for woord in meervoud_zelfstandig_naamwoorden]
    enkelvoud_zelfstandig_naamwoorden = enkelvoud_zelfstandig_naamwoorden + [woord.title() for woord in enkelvoud_zelfstandig_naamwoorden]


    for woord in meervoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'zombies', tekst)
    for woord in enkelvoud_zelfstandig_naamwoorden:
        tekst = re.sub(r'\b{0}\b'.format(woord), 'zombie', tekst)
    for word in spreken:
        tekst = re.sub(r'\b{0}\b'.format(woord), choice(zombie_geluiden), tekst)
    return(tekst)
    

def zombificeer_spraak(tekst): 
    tekst = re.sub(r'[eiosEIOS]', 'r', tekst)
    tekst = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', tekst)
    tekst = re.sub(r'r\b', 'rh', text)
    tekst = re.sub(r'(\b[aA]\b)','hra', tekst)
    return tekst

tekst = verander_proza(tekst)

spraak = re.findall(r'“.*?”', tekst, flags=re.DOTALL)

with open('Zombie.txt', 'w', encoding="utf-8") as f:
    f.write(tekst)
```

- De laatste stap is om alle spraak in het boek te doorlopen en te vertalen in zombietaal. Dit kan gebeuren voordat je de functie `proza_veranderen()` aanroept.

```python
for woorden in spraak:
    tekst = tekst.replace(woorden, zombificeer_spraak(woorden))
```

- Voer nu je code uit en bekijk de zombieversie van _Pride en Prejudice_ die nu moet zijn opgeslagen.

