import requests
import re
from random import choice

#book = requests.get("https://www.gutenberg.org/files/1342/1342-0.txt")
book_text = book.text

result = re.findall('(?<=Chapter 3)(.*?)(?=Chapter 4)', book_text, flags=re.S)

chapter_1 = result[0]

speech = re.findall('(?<=“)(.*?)(?=”)', chapter_1, flags=re.S)

## Zombie language rules
'''
- all occurrences of characters "eiou" (case-insensitive) are replaced with "r".
- all characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.
- multiple spaces are replaced with a single.
- lower-case "r" at the end of words replaced with "rh".
- an "a" or "A" by itself will be replaced with "hra".
- the starts of sentences are capitalised (the "start of a sentence" is any occurrence of ".!?", followed by a space, followed by a letter.)
- spaces preceding any of ".!?" are stripped.
- the first character is capitalised.
'''
translator = {words:words for words in speech}

def replace_eios(words):
    for char in 'eiosEIOS':
        words = words.replace(char, 'r')
    return words

def strip_chars(words):
    for char in words:
        if char.lower() not in 'zhrgbmna .!?-':
            words = words.replace(char, '')
    return words

def replace_a(words):
    end_of_word = '.,!?;: '
    for char in end_of_word:
        words = words.replace(' a'+char, ' hra ')
        words = words.replace(' A'+char, ' hra ')
    return words

for words in translator.keys():
    translator[words] = replace_a(translator[words])
    translator[words] = replace_eios(translator[words])
    translator[words] = strip_chars(translator[words])

for words in translator.keys():
    if words in chapter_1:
        chapter_1 = chapter_1.replace(words, translator[words])

singular_nouns = [' Son ', ' Daughter ', ' Child ',' Wife ', ' Woman ', ' Mrs. ', ' Miss ',' Husband ', ' Man ', ' Mr. ', ' Sir ', ' Lady ']
plural_nouns = [' Ladies ', ' Gentlemen', ' Women ', ' Men ', ' Children ', ' Boys ', ' Girls ']
speaking = ['said', 'replied', 'spoke', 'shouted', 'cried']

for word in singular_nouns:
    chapter_1 = chapter_1.replace(word, 'Zombie')
    chapter_1 = chapter_1.replace(word.lower(), 'zombie')

for word in plural_nouns:
    chapter_1 = chapter_1.replace(word, 'Zombies')
    chapter_1 = chapter_1.replace(word.lower(), 'zombies')

for word in speaking:
    chapter_1 = chapter_1.replace(word, choice(['groaned', 'moaned', 'grunted', 'growled']))

with open('chapter_1.txt', 'w') as f:
    f.write(chapter_1)
