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

- You could change all the words in you lists, so that instead of `'ladies'` and `'gentlemen'` you have `r'\bladies\b'` and `r'\bgentlemen\b'`, for instance. But that seems a lot of work. It's easier to use the amazing `.format()` method in Python for this job.

[[[generic-python-simple-string-formating]]]

- Now try using `.format()` within your `re.sub()` methods, to automatically turn `'ladies'` into `'\bladies\'`, for instance.

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
