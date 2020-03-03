## Zombie language - rule 2

The second rule for converting English into zombie language is:

- All characters other than "zhrgbmna .!?-" (case-insensitive) are taken out.

To do this, you can search for multiple characters again. But this time you want to exclude certain characters from the regex search.

[[[generic-python-regex-excluding-patterns]]]

- Use the information above to replace all the characters except for `zhrgbmna?\n .!?-` with an empty string (`""`).

--- hints --- --- hint ---

- Don't forget that you need to exclued upper- and lower-case characters.

  ```python
  zhrgbmnaZHRGBMNA“”?\n .!?-
  ```

--- /hint --- --- hint ---

- The pattern you are looking to exclude therefore becomes:

  ```python
  r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]'
  ```

--- /hint --- --- hint ---

- Your full substitution will look like this:

  ```python
  text = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', text)
  ```
  
--- /hint --- --- /hints ---
