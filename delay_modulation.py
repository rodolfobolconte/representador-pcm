import numpy as np

from desenha_grafico import *

def delay_modulation(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	zeroDuplo = False

	taxa_amostragem = 20

	for b in range(len(sequencia)):
		if sequencia[b] == '1':
			if sinal[-1] == 1:
				
				y1 = [1.0] * taxa_amostragem ; y2 = [-1.0] * taxa_amostragem
				y = list(y1) + list(y2)

				sinal += list(y)

			else:

				y1 = [-1.0] * taxa_amostragem ; y2 = [1.0] * taxa_amostragem
				y = list(y1) + list(y2)

				sinal += list(y)

		elif sequencia[b] == '0':

			if zeroDuplo:

				y = [-1.0] * taxa_amostragem * 2

				sinal += list(y)

				zeroDuplo = False

			elif sequencia[b-1] == '0' and not zeroDuplo:

				y = [1.0] * taxa_amostragem * 2

				sinal += list(y)

				zeroDuplo = True

			else:

				y = [-1.0] * taxa_amostragem * 2

				sinal += list(y)

	qt_amostras = taxa_amostragem * 1600 / 50

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "delay modulation")