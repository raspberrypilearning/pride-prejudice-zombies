import re

sentence = "The men of the establishment were managing to manoeuvre the mentors."

plural_nouns = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']

singular_nouns = ['son', 'daughter', 'child','wife', 'woman', 'mrs', 'miss','husband', 'man', 'mr', 'sir', 'lady']

for word in plural_nouns:
    sentence = re.sub(r'\b{0}\b'.format(word), 'zombies', sentence)
for word in singular_nouns:
    sentence = re.sub(r'\b{0}\b'.format(word), 'zombie', sentence)

print(sentence)
