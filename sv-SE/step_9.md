## Adding functions
- Your code should look something like this now:

    ```python
    import re
    from random import choice
    import requests

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    r = requests.get(url)
    text = r.text

    plural_nouns = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']

    singular_nouns = ['son', 'daughter', 'child','wife', 'woman', 'mrs', 'miss','husband', 'man', 'mr', 'sir', 'lady']

    speaking = ['said', 'replied', 'spoke', 'shouted', 'cried']
    zombie_sounds = ['groaned', 'moaned' ,'growled', 'screamed', 'gurgled']

    plural_nouns = plural_nouns + [word.title() for word in plural_nouns]
    singular_nouns = singular_nouns + [word.title() for word in singular_nouns]


    for word in plural_nouns:
        text = re.sub(r'\b{0}\b'.format(word), 'zombies', text)
    for word in singular_nouns:
        text = re.sub(r'\b{0}\b'.format(word), 'zombie', text)
    for word in speaking:
        text = re.sub(r'\b{0}\b'.format(word), choice(zombie_sounds), text)

    with open('Zombie.txt', 'w', encoding="utf-8") as f:
        f.write(text)
    ```

- If you run the code, and then look in your directory, you should see a new file created called **Zombie.txt**. Have a look at the file by opening it with any text editor.

- The first paragraph of Chapter 1 should now read: **It is a truth universally acknowledged, that a single zombie in possession of a good fortune, must be in want of a zombie.**

- The first time somebody in the book speaks, it should read something like: **“My dear zombie. Bennet,” moaned his zombie to him one day, “have you heard that Netherfield Park is let at last?”**

- Compare your code with the version above if it is not working.

- Now you want to tidy your code up a little before moving onto the next part. Place the core code that converts the text into a **function** and then call it.

    ```python
    import re
    from random import choice
    import requests

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    r = requests.get(url)
    text = r.text

    def change_prose(text):
        plural_nouns = ['ladies', 'gentlemen', 'women', 'men', 'children', 'boys', 'girls']

        singular_nouns = ['son', 'daughter', 'child','wife', 'woman', 'mrs', 'miss','husband', 'man', 'mr', 'sir', 'lady']

        speaking = ['said', 'replied', 'spoke', 'shouted', 'cried']
        zombie_sounds = ['groaned', 'moaned' ,'growled', 'screamed', 'gurgled']

        plural_nouns = plural_nouns + [word.title() for word in plural_nouns]
        singular_nouns = singular_nouns + [word.title() for word in singular_nouns]


        for word in plural_nouns:
            text = re.sub(r'\b{0}\b'.format(word), 'zombies', text)
        for word in singular_nouns:
            text = re.sub(r'\b{0}\b'.format(word), 'zombie', text)
        for word in speaking:
            text = re.sub(r'\b{0}\b'.format(word), choice(zombie_sounds), text)
        return(text)

    text = change_prose(text)

    with open('Zombie.txt', 'w', encoding="utf-8") as f:
        f.write(text)
    ```
