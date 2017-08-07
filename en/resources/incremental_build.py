import re
from random import choice

text = '"I am tired", the man said'

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
                      
print(text)
