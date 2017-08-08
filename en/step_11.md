## Rule 2

The second rule for the zombie language is:

**all characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.**

- To do this, you can search for multiple characters again. This time though, you want to be excluding certain characters from the **regex** search.

[[[generic-python-regex-excluding-patterns]]]

- Use the information above to replace all the characters except for `zhrgbmna?\n .!?-` with an empty string (`""`).

--- hints --- --- hint ---
- Don't forget that you need to exclued upper and lowercase characters.
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
