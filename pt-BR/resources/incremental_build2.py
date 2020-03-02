import re

text = 'The quick brown fox jumped over the lazy dog'

def zombify_speech(text):
	text = re.sub(r'[eiosEIOS]', 'r', text)
	text = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', text)
	text = re.sub(r'r\b', 'rh', text)
	text = re.sub(r'(\b[aA]\b)','hra', text)
	return text

text = zombify_speech(text)
