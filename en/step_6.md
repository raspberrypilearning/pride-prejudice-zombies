## The zombies are on the case

- So far, apart from the lists of words you generate and the imports, your basic logic should look something like this:

	```python
	for word in plural_nouns:
		sentence = re.sub(r'\b{0}\b'.format(word), 'zombies', sentence)
	for word in singular_nouns:
		sentence = re.sub(r'\b{0}\b'.format(word), 'zombie', sentence)
	```

- This works fine for most sentences, but it will fall over for the following sentence.

```python
sentence = 'Ladies and Gentlemen, will the boys and girls please leave''
```

- This is because our regex substitutions are case sensitive. So while `ladies` will be changed to `zombies`, `Ladies` will not.

- It is possible to ignore case in a regex search, but that would just make everything lower case, and zombies hate bad grammar, so that's not the best solution.

- Instead you can make your lists contain words starting with upper case and lower case letters using two little tricks - **list comprehensions** and **case operations**

[[[generic-python-string-operations-case]]]
[[[generic-python-simple-list-comprehensions]]]

- Using **case operations** and **list comprehensions** you can turn:
  ```python
  ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']
  ```
  into the following:
  ```python
  ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls', 'Ladies', 'Gentlemen', 'Women', 'Men', 'Children', 'Boys', 'Girls']
  ```
  
- Have a try, and use the hints below if you need help. You'll need to convert both noun lists.

--- hints --- --- hint ---
- `ladies` can be turned into `Ladies` using the `.title()` operation.
	```python
	>>> 'ladies'.title()
	'Ladies'
	```
--- /hint --- --- hint ---
- The basic structure of the list comprehension would be something like:

	```python
	[word.title() for word in plural_nouns]
	```
--- /hint --- --- hint ---
- The full list comprehension would be:
  ```python
  plural_nouns = plural_nouns + [word.title() for word in plural_nouns]
  ```
- The same needs to be done for the singular nouns.
--- /hint --- --- /hints ---
