import re

texto = 'El veloz zorro marrón saltó sobre el perro perezoso'

def zombificar_discurso(texto):
	texto = re.sub(r'[eiosEIOS]', 'r', texto)
	texto = re.sub(r'[^zhrgbmnaZHRGBMNA“”?\n .!?-]', '', texto)
	texto = re.sub(r'r\b', 'rh', texto)
	texto = re.sub(r'(\b[aA]\b)','hra', texto)
	return texto

texto = zombificar_discurso(texto)
