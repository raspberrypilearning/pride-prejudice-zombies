## Making it all about zombies

- First you're going to figure out how to change a simple sentence so it is all about zombies.

	```
	The woman laughed at the silly men.
	```

- There are only two words to be replaced to begin with: `'woman'` and `'men'`. The first needs to become `'zombie'` and the second needs to become `'zombies'`.

- To replace these words, you can use **reg**ular **ex**pressions, or regex. Regex allows you to find **patterns** of characters in text. Have a look at the section below, and see if you can figure out how to convert the above sentence so that it reads:

	```
	The zombie laughed at the silly zombies.
	```
	
[[[generic-python-regex-substitute-simple-pattern]]]

--- hints --- --- hint ---
Begin by importing the `re` module and creating the string you want to alter.
```python
import re
text = 'The woman laughed at the silly men.'
```
--- /hint --- --- hint ---
Now you want to use the `re.sub()` method to first change `'woman'` to `'zombie'`, and then use it again to change `'men'` to `'zombies'`.
```python
new_text = re.sub('pattern to find', 'pattern to replace', text)
```
--- /hint --- --- hint ---
You first substitution would therefore look like this.
```python
re.sub('woman', 'zombie', text)
```
Now you just need to repeat this line but use `'men'` and `'zombies'`.
--- /hint --- --- /hints ---
