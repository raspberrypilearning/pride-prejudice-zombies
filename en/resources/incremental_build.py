import re
from random import choice
import requests

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
r = requests.get(url)
text = r.text

def change_prose(text):
    plural_nouns = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']

    singular_nouns = ['son', 'daughter', 'child','wife', 'woman', 'mrs', 'miss','husband', 'man', 'mr', 'sir', 'lady']

    speaking = ['said', 'replied', 'spoke', 'shouted', 'cried']
    zombie_sounds = ['groaned', 'moaned' ,'growled', 'screamed', 'gurgled']

    plural_nouns = plural_nouns + [word.title() for word in plural_nouns]
    singular_nouns = singular_nouns + [word.title() for word in singular_nouns]


    for word in plural_nouns:
        text = re.sub(r'\b{0}\b'.format(word), 'zombies', text)
    for word in singular_nouns:
        text = re.sub(r'\b{0}\b'.format(word), 'zombie', text)
    for word in speaking:
        text = re.sub(r'\b{0}\b'.format(word), choice(zombie_sounds), text)
    return(text)


def zombify_speech(text):
	text = re.sub(r'[eiosEIOS]', 'r', text)
	text = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', text)
	text = re.sub(r'r\b', 'rh', text)
	text = re.sub(r'(\b[aA]\b)','hra', text)
	return text

speech = re.findall(r'“.*?”', text, flags=re.DOTALL)

for i in speech:
    text = text.replace(i, zombify_speech(i))
    
with open('Zombie.txt', 'w') as f:
    f.write(text)
