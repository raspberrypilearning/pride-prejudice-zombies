## Zombie language - rules 3 and 4

Rule 3 states that lower-case 'r' characters at the end of words need to be replaced with 'rh'.

- You've learned how to use `\b` to look for patterns at the beginning and end of words.

[[[generic-python-regex-substitute-word-boundaries]]]

- You now need to construct a pattern to search for `'r'` characters at the end of a word, and replace them with `'rh'`

- To follow rule 4, you will need another replacement pattern that looks for the characters `'a'` and `'A'` when they are on their own, and replaces them with `'hra'`

--- hints --- --- hint ---

- The first pattern you are searching for is `r'r\b'`.

--- /hint --- --- hint ---

- Your full substitution will look like this:

```python
text = re.sub(r'r\b', 'rh', text)
```

--- /hint --- --- hint ---

- To find single `a` or `A` characters, you can use the `r'(\b[aA]\b)'` pattern.

```python
text = re.sub(r'(\b[aA]\b)','hra', text)
```

--- /hint --- --- /hints ---
