## The zombies are on the case

- So far, apart from the lists of words you generated and the imports, your script's basic logic should look something like this:

	```python
	for word in plural_nouns:
		text = re.sub(r'\b{0}\b'.format(word), 'zombies', text)
	for word in singular_nouns:
		text = re.sub(r'\b{0}\b'.format(word), 'zombie', text)
	```

- This works fine for most texts, but it will fail in the following example:

```python
text = 'Ladies and Gentlemen, will the boys and girls please leave''
```

- This is because our regex substitutions are case-sensitive. So while `'ladies'` will be changed to `'zombies'`, `'Ladies'` won't be changed.

- It is possible to ignore case in a regex search, but that would just make everything lower case, and zombies hate bad grammar, so it's not the best solution.

- Instead you can create new lists containing words starting with upper case and lower case letters using two little tricks: **list comprehensions** and **case operations**.

[[[generic-python-string-operations-case]]]
[[[generic-python-simple-list-comprehensions]]]

- You can use **case operations** and **list comprehensions** to use this:
  ```python
  ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']
  ```
  to create the following:
  
  ```python
  ['Ladies', 'Gentlemen', 'Women', 'Men', 'Children', 'Boys', 'Girls']
  ```
  
- Use what you have learned to create two **new** lists called `plural_nouns_title` and `singular_nouns_title`.

--- hints --- --- hint ---
- `'ladies'` can be turned into `'Ladies'` using the `.title()` operation.
	```python
	>>> 'ladies'.title()
	'Ladies'
	```
--- /hint --- --- hint ---
- The basic structure of the list comprehension would be something like this:

	```python
	[word.title() for word in plural_nouns]
	```
--- /hint --- --- hint ---
- The full list comprehension will be:
  ```python
  plural_nouns_title = [word.title() for word in plural_nouns]
  ```
- The same needs to be done for the singular nouns.
--- /hint --- --- /hints ---

- Now you will need an additional **two** `for` loops. One for `plural_nouns_title` and one for `singular_nouns_title`.

	```python
	for word in plural_nouns_title:
		text = re.sub(r'\b{0}\b'.format(word), 'Zombies', text)
	for word in singular_nouns_title:
		text = re.sub(r'\b{0}\b'.format(word), 'Zombie', text)
	```
