## Zombie language

Although all the prose has now been changed to make the book more appropriate for zombies, all the speech within the book is still in plain English.

Although zombies can understand English, that's not the way they speak. It isn't well-known, but there are actually some strict rules regarding how English is translated into zombie language:

1. All occurrences of the characters 'eiou' (case-insensitive) needs to be replaced with 'r'
1. All characters other than 'zhrgbmna .!?-' (case-insensitive) are taken out
1. Any lower-case 'r' at the end of a word is replaced with 'rh'
1. An 'a' or 'A' by itself has to be replaced with 'hra'

- Once again regex can help us out with this task. Rather than trying this out on the entire book straight away, **create a new Python file**, so that you can practice on a few sample sentences.

# Rule 1

- Try and convert the following text using the first rule.

    ```python
    import re
    text = 'The quick brown fox jumped over the lazy dog'
    ```

- Have a look at the section below to learn how to substitute multiple different characters with regex.

[[[generic-python-regex-substitute-multiple-characters]]]

- Now use regex to complete rule 1.

--- hints --- --- hint ---
- You need to convert all the `'e'`,`'i'`,`'o'`, and `'s'` characters, whether they are upper case or lower case, into `'r'` characters. --- /hint --- --- hint ---
- The regex pattern you should be looking for is `[eiosEIOS]`. --- /hint --- --- hint ---
- The text can be converted with a single line:
    ```python
    text = re.sub(r'[eiosEIOS]', 'r', text)
    ```
--- /hint --- --- /hints ---
