## THIS IS AN EXPLANATION OF THE LAMBDA FUNCTION EQIVALENT

import re

def f(match):
    print(match.group())
    if match.group()[0].isupper():
        return 'Zombie'
    else:
        return 'zombie'

string = 'A better mannered man called Man for all of Mankind'

find = '[Mm]an'
broad = re.sub(r'{0}'.format(find), f, string)
narrow = re.sub(r'\b{0}\b'.format(find), f, string)

