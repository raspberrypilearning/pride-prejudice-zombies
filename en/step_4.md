## Multiple similar replacements

- What about a more complicated passage of text.

	```python
	text = "The boys and girls laughed at the woman's joke. The man did not find it so funny."
	```
	
- There are now two groups of nouns that need replacing. Singular nounds like `woman` and `man` and plural nouns like `boys` and `girls`.

- How could this text be easily zombiefied, without too many lines of code.

- Tackling the plural nouns first, if they were in a **list** then you could use a `for` loop to replace each of the words in the list.

[[[generic-python-for-loop-list]]]

- First create a list of plural nounds that might need changing to the word `zombies`. 

	```python
	plural_nouns = plural_nouns = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']
	```

- Now you need to iterate over the list, and use `re.sub()` on each word.

	```python
	for word in plural_nouns:
	    text = re.sub(word, 'zombies', text)
	print(text)
	```
	
- You should see the following printed out:

	```
	The zombies and zombies laughed at the woman's joke. The man did not find it so funny.
	```

- Now try and write a second `for` loop that can iterate over a list of singular_nouns, and replace them with `'zombie'`. Here's a list to start you off:

	```python
	singular_nouns = ['son', 'daughter', 'child','wife', 'woman', 'mrs', 'miss','husband', 'man', 'mr', 'sir', 'lady']
	```
	
--- hints --- --- hint ---
- Your second `for` loop should start beneath the first, but outside of it.

--- /hint --- --- hint ---
- Here's some code to start you off:
```python
for word in plural_nouns:
	text = re.sub(word, 'zombies', text)
for word in singular_nouns:
```
--- /hint --- --- hint ---
- Use `re.sub(word, 'zombie', text)` to convert the words in the text.
--- /hint --- --- /hints ---
