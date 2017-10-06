## Finishing the zombie-friendly book

- You now need to bring everything: your function for altering the prose, your function for translating speech, and your search for speech.

- Your file should look something like this:

	```python
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

	text = change_prose(text)
	
	speech = re.findall(r'“.*?”', text, flags=re.DOTALL)

	with open('Zombie.txt', 'w', encoding="utf-8") as f:
		f.write(text)
	```

- The last step is to run through all of the speech in the book, and translate it into zombie language. This can go just before you call the `change_prose()` function.

```python
for words in speech:
    text = text.replace(words, zombify_speech(words))
```

- Now run your code and have a look at the zombie version of _Pride and Prejudice_ that should now be saved.

