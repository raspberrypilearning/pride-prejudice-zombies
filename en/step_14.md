## Finding speech

- The next stage is to find all the speech in the **Pride and Prejudice** book, and run it through your translator.

- To do this, let's first have a look at some speech from the book.

```
“My dear Mr. Bennet,” said his lady to him one day, “have you heard that Netherfield Park is let at last?”
```

- You'll notice that the speech is contained between double quotes. These aren't the normal quotes that you find on your computer keyboard though. Look closely and you should see that both `“` and `”` are different to `"`.

- Again, regular expressions can be used to find all the text between any two characters.

[[[generic-python-regex-text-between-patterns]]]

- Now you want to search the text in the book and find all strings surrounded by `“` and `”`. Remember these are not normal double quotes, to you need to copy and paste them from this page. Store the generated list with the name `speech`.

--- hints --- --- hint ---
Use `re.findall` with a pattern matching everything between `“` and `”`.
--- /hint --- --- hint ---
There's no need to use look ahead or look behind in this search, but you are looking at multi-line stings, so the `re.DOTALL` flag will be needed.
--- /hint --- --- hint ---
Your search should look like this:
```python
text = “My dear Mr. Bennet,” said his lady to him one day, “have you heard that Netherfield Park is let at last?”
speech = re.findall(r'“.*?”', text, flags=re.DOTALL)
```
--- /hint --- --- /hints ---
