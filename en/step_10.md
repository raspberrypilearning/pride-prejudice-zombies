## Zombie language

Although all the prose have now been changed to make the book more appropriate for zombies, all the speech within the book is still in plain English.

Although zombies can understand English, that's not the way they speak. It isn't well known, but there are actually some strict rules regarding how English is translated into zombie language.

Here are the rules:
1. all occurrences of characters "eiou" (case-insensitive) are replaced with "r".
1. all characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.
1. lower-case "r" at the end of words replaced with "rh"
1. an "a" or "A" by itself will be replaced with "hra"

- Once again **regex** can help us out with this task. Rather than trying this straight out on the entire book, create a new Python file, so that you can practice on a few sample sentences.

- Now you can try and use convert the text, using the first rule.

	```python
	import re
	text = 'The quick brown fox jumped over the lazy dog'
	```

- Have a look at the section below to learn how to substitute multiple difference characters with **regex**

[[[generic-python-regex-substitute-multiple-characters]]]

- Now use **regex** to complete rule 1.

--- hints --- --- hint ---
- You need to convert all the `e`,`i`,`o`, and `s` characters, whether they are uppercase or lowercase into `r` characters.
--- /hint --- --- hint ---
- The **regex** pattern you should be looking for is `[eiosEIOS]`
--- /hint --- --- hint ---
- The text can be converted with a single line:
	```python
	text = re.sub(r'[eiosEIOS]', 'r', text)
	```
--- /hint --- --- /hints ---
