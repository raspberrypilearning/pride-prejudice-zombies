## Putting the translator together

- You can now put all the substitutions together.

	```python
	import re
	text = 'The quick brown fox jumped over the lazy dog'

	def zombify_speech(text):
		text = re.sub(r'[eiosEIOS]', 'r', text)
		text = re.sub(r'[^zhrgbmnaZHRGBMNA?\n .!?-]', '', text)
		text = re.sub(r'r\b', 'rh', text)
		text = re.sub(r'(\b[aA]\b)','hra', text)
		return text

	text = zombify_speech(text)
	```
- If you run your program and then query the value of `text` in the interpreter, you should see the following.

	```python
	>>> text
	'hrh rh brrn rh mrh rrrh hrh az rg'
	```
