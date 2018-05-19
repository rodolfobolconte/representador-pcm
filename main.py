from tkinter import *
from functools import partial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

janela_principal = Tk()
janela_principal.title("Representador de Forma PCM (Pulse Code Modulation)")
janela_principal.configure(background='white')

fig, eixo = plt.subplots(nrows=1, ncols=1, figsize=(80, 7))
canvas = FigureCanvasTkAgg(fig, master=janela_principal)

def desenha_grafico(x, y, sequencia, tipo_pcm):
	global fig, eixo, canvas

	canvas.get_tk_widget().destroy()

	fig, eixo = plt.subplots(nrows=1, ncols=1)

	grafico = eixo.plot(x, y)

	eixo.set_xticks(np.arange(0.0, len(sequencia) + 0.5, 1))
	eixo.set_yticks(np.arange(-1.5, 2., 0.5))

	eixo.set_title("Sequência digitada para " + tipo_pcm.upper() + ": " + sequencia)
	eixo.grid(True)

	canvas = FigureCanvasTkAgg(fig, master=janela_principal)
	canvas.show()
	canvas.get_tk_widget().pack(fill=BOTH, expand=1, padx=150, pady=30)

	menu(janela_principal)

def nrz_l(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	taxa_amostragem = 20

	for b in range(len(sequencia)):
		
		if sequencia[b] == '1': y = [1.0] * taxa_amostragem * 2
		elif sequencia[b] == '0': y = [-1.0] * taxa_amostragem * 2

		sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "nrz-l")

def nrz_m(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [-1]

	taxa_amostragem = 20

	for b in range(len(sequencia)):
		if sequencia[b] == '1':

			if sinal[-1] == 1: y = [-1.0] * taxa_amostragem * 2
			else: y = [1.0] * taxa_amostragem * 2

			sinal += list(y)

		elif sequencia[b] == '0':

			if sinal[-1] == 1: y = [1.0] * taxa_amostragem * 2
			else: y = [-1.0] * taxa_amostragem * 2

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "nrz-m")

def nrz_s(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [-1]

	taxa_amostragem = 20

	for b in range(len(sequencia)):
		if sequencia[b] == '0':

			if sinal[-1] == 1: y = [-1.0] * taxa_amostragem * 2
			else: y = [1.0] * taxa_amostragem * 2

			sinal += list(y)

		elif sequencia[b] == '1':

			if sinal[-1] == 1: y = [1.0] * taxa_amostragem * 2
			else: y = [-1.0] * taxa_amostragem * 2

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "nrz-s")

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

def menu(janela_principal):
	

	label_digitar_sequencia = Label(janela_principal, text="Digite a sequência de 16 bits:", font=14, bg='white')
	label_digitar_sequencia.place(x=10, y=10)

	caixa_de_texto = Entry(janela_principal, width=16, font=14, bg='#DDD')
	caixa_de_texto.place(x=10, y=40)

	label_digitar_sequencia = Label(janela_principal, text="Escolha o tipo do PCM:", font=14, bg='white')
	label_digitar_sequencia.place(x=10, y=70)

	botao_nrz_l = Button(janela_principal, width=16, font=None, text="NRZ-L", command=nrz_l)
	botao_nrz_l.place(x=10, y=100)

	botao_nrz_m = Button(janela_principal, width=16, font=None, text="NRZ-M", command=nrz_m)
	botao_nrz_m.place(x=10, y=130)

	botao_nrz_s = Button(janela_principal, width=16, font=None, text="NRZ-S", command=nrz_s)
	botao_nrz_s.place(x=10, y=160)

	botao_delay_modulation = Button(janela_principal, width=16, font=None, text="Delay Modulation", command=delay_modulation)
	botao_delay_modulation.place(x=10, y=190)
	

	botao_delay_modulation["command"] = partial(delay_modulation, janela_principal, caixa_de_texto)
	botao_nrz_l["command"] = partial(nrz_l, janela_principal, caixa_de_texto)
	botao_nrz_m["command"] = partial(nrz_m, janela_principal, caixa_de_texto)
	botao_nrz_s["command"] = partial(nrz_s, janela_principal, caixa_de_texto)

	
menu(janela_principal)

janela_principal.geometry("{0}x{1}+0+0".format(janela_principal.winfo_screenwidth(), janela_principal.winfo_screenheight()))
janela_principal.mainloop()