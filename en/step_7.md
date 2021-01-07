## Zombies moan and groan

- Let's change the text that you're working on.
  ```python
  text = '"I am tired", the man said'
  ```

- Zombies don't say things, they groan, moan and growl. So the text needs further alteration.

- Start by making a list of words that indicate speech. Here are a few examples:

	```python
	speaking = ['said', 'replied', 'spoke', 'shouted', 'cried', 'whispered']
	```

- Then make another list using words that describe how zombies sound. Here are a few you might like to start with:

	```python
	zombie_sounds = ['groaned', 'moaned' ,'growled', 'screamed', 'gurgled']
	```

- Now you can use another for loop to replace every word in the text that is in the `speaking` list with a random word from the `zombie_sounds` list.

- First you'll need to import the `choice` method from the `random` module.

	```python
	import re
	from random import choice
	```

- Then construct the for loop, using the same regex substitution method you used before, but this time using a random item from `zombie_sounds`.

	```python
	for word in speaking:
		text = re.sub(r'\b{0}\b'.format(word), choice(zombie_sounds), text)
	```
	
- Running your code now should give you the following output, with the final word randomly chosen from the list.

```python
>>> "I am tired", the zombie groaned
```
