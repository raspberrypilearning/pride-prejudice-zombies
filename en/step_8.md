## Zombie Austen

- So far you've been working on just a few sentences, but the code you have written will work on large texts as well.

- There are a huge number of books in the public domain. They are available on the [Project Gutenberg website](https://www.gutenberg.org/). Included in the archive is Jane Austen's book [*Pride and Prejudice*](https://www.gutenberg.org/files/1342/1342-0.txt).

- You can use Python to fetch this book from the website, but you'll need to use the `requests` module. Import the module along with your other modules.

	```python
	import re
	from random import choice
	import requests
	```

- Now use the `requests` module to fetch the book at https://www.gutenberg.org/files/1342/1342-0.txt, and store its text using the variable name `text`.

[[[generic-python-requests]]]

- Once you have the text, it's probably best to write the data out to a file, rather than printing it.

[[[generic-python-writing-to-a-file]]]

--- hints --- --- hint ---
- First you need to fetch the page data:
  ```python
  url = "https://www.gutenberg.org/files/1342/1342-0.txt"
  r = requests.get(url)
  ```
--- /hint --- --- hint ---
- The text can then be extracted from the data. First delete the line where you currently set `text` to whatever string you were experimenting with. Then replace it with this:
  ```python
  text = r.text
  ```
--- /hint --- --- hint ---
- Rather than printing the text, you should write it out to a file. So delete any `print(text)` lines you have, and instead use this:
  ```python
  with open('Zombies_Version.txt', 'w') as f:
	  f.write(text)
  ```
--- /hint --- --- /hints ---
