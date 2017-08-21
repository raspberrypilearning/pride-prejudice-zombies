## Zombies everywhere

- There's a problem with your script as it is now. Consider this sentence:

	```
	text = "The men of the establishment were managing to manoeuvre the mentors."
	```

- Change the text in your script to the one above, and run it again. This time your text will look a little odd.

	```
	The zombies of the establishzombiest were zombieaging to zombieoeuvre the zombiestors.
	```

- That's way too many zombies! Any `'man'` or `'men'` pattern within the text has been changed to `'zombie'`, so for example the word `'mentors'` is now `'zombiestors'`. How can this be solved?

- Luckily, the clever people that came up with regex thought about this, and there's a way of only matching whole words.

[[[generic-python-regex-substitute-word-boundaries]]]

- Using `r'\bman\b'` as your search pattern, would only find the specific word `man`. You could then use `re.sub()` to swap out `man` for `zombie`. This would mean using lots of loops though; one for each substitution. Using the `.format` method in Python can ensure you only use two loops; one for plural nouns and one for singular nouns.

[[[generic-python-simple-string-formating]]]

- Now try using `.format()` within your `re.sub()` methods, to automatically turn `'ladies'` into `'zombies'` and `'gentlemen'` into `'zombies'`.

--- hints --- --- hint ---
- Here's how you can set up the pattern you are after.
```python
r'\b{0}\b'.format(word)
```
--- /hint --- --- hint ---
- Within one of your for loops, it would look like this:
```python
for word in plural_nouns:
	text = re.sub(r'\b{0}\b'.format(word), 'zombies', text)
```
- Now you should be able to do the second for loop by yourself.
--- /hint --- --- /hints ---
