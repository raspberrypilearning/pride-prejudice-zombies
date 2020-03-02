from random import choice
import re

book = open('pp.txt','r')
text = book.read()

def find_speech(words):
    speech = re.findall(r'“.*?”',words, flags=re.DOTALL)
    #speech = re.findall(r'(?=“)(.*?)(?<=”)',words, flags=re.DOTALL)
    return speech

def replace_eios(words):
    '''all occurrences of characters "eiou" (case-insensitive) are replaced with "r".'''
    words = re.sub(r'[eiosEIOS]', 'r', words)
    return words

def strip_chars(words):
    '''all characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.'''
    words = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', words)
    return words

def replace_terminal_r(words):
    '''lower-case "r" at the end of words replaced with "rh".'''
    words = re.sub(r'r\b', 'rh', words)
    return words

def replace_a(words):
    '''an "a" or "A" by itself will be replaced with "hra".'''
    words = re.sub(r'(\b[aA]\b)','hra',words)
    return words

def zombify_speech(words):
    words = replace_eios(words)
    words = strip_chars(words)
    words = replace_terminal_r(words)
    words = replace_a(words)
    return words

def zombify_prose(words):
    singular_nouns = ['Son', 'Daughter', 'Child','Wife', 'Woman', 'Mrs', 'Miss','Husband', 'Man', 'Mr', 'Sir', 'Lady']
    plural_nouns = ['Ladies', 'Gentlemen', 'Women', 'Men', 'Children', 'Boys', 'Girls']
    speaking = ['Said', 'Replied', 'Spoke', 'Shouted', 'Sried']
    for word in singular_nouns:
        words = re.sub(r'\b{0}\b'.format(word), 'Zombie', words)
        words = re.sub(r'\b{0}\b'.format(word.lower), 'zombie', words)

    for word in plural_nouns:
        words = re.sub(r'\b{0}\b'.format(word), 'Zombies', words)
        words = re.sub(r'\b{0}\b'.format(word.lower()), 'zombies', words)

    for word in speaking:
        words = re.sub(word, choice(['groaned', 'moaned', 'grunted', 'growled']), words)
    return words

for speech in find_speech(text):
    text = text.replace(speech, zombify_speech(speech))

text = zombify_prose(text)

with open('Zombies_Version.txt', 'w') as file:
    file.write(text)
