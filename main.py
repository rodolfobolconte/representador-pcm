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

taxa_amostragem = 20

def nrz_l(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

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

def unipolar_rz(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	for b in range(len(sequencia)):
		if sequencia[b] == '1':

			y1 = [1.0] * taxa_amostragem ; y2 = [0] * taxa_amostragem
			y = list(y1) + list(y2)

			sinal += list(y)

		elif sequencia[b] == '0':

			y = [0] * taxa_amostragem * 2

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "unipolar rz")

def bipolar_rz(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	for b in range(len(sequencia)):
		if sequencia[b] == '1':

			y1 = [1.0] * taxa_amostragem ; y2 = [0] * taxa_amostragem
			y = list(y1) + list(y2)

			sinal += list(y)

		elif sequencia[b] == '0':

			y1 = [-1.0] * taxa_amostragem ; y2 = [0] * taxa_amostragem
			y = list(y1) + list(y2)

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "bipolar rz")

def rz_ami(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [0]

	alternador = 1

	for b in range(len(sequencia)):
		if sequencia[b] == '1':

			y1 = [0] * int(taxa_amostragem / 2)
			y2 = [alternador] * taxa_amostragem
			y3 = [0] * int(taxa_amostragem / 2)

			alternador = -alternador

			y = list(y1) + list(y2) + list(y3)

			sinal += list(y)

		elif sequencia[b] == '0':

			y = [0] * taxa_amostragem * 2

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "rz-ami")

def bi_phase_l(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [0]

	for b in range(len(sequencia)):
		if sequencia[b] == '1':

			y1 = [1] * taxa_amostragem
			y2 = [-1] * taxa_amostragem

			y = list(y1) + list(y2)

			sinal += list(y)

		elif sequencia[b] == '0':

			y1 = [-1] * taxa_amostragem
			y2 = [1] * taxa_amostragem

			y = list(y1) + list(y2)

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "bi-phase-l")

def bi_phase_m(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	for b in range(len(sequencia)):
		if sequencia[b] == '1':

			if sinal[-1] == 1:
				y1 = [-1] * taxa_amostragem
				y2 = [1] * taxa_amostragem

			else:
				y1 = [1] * taxa_amostragem
				y2 = [-1] * taxa_amostragem

			y = list(y1) + list(y2)

			sinal += list(y)

		elif sequencia[b] == '0':
			
			if sinal[-1] == 1: y = [-1] * taxa_amostragem * 2
			else: y = [1] * taxa_amostragem * 2

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "bi-phase-m")

def bi_phase_s(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	for b in range(len(sequencia)):
		if sequencia[b] == '0':

			if sinal[-1] == 1:
				y1 = [-1] * taxa_amostragem
				y2 = [1] * taxa_amostragem

			else:
				y1 = [1] * taxa_amostragem
				y2 = [-1] * taxa_amostragem

			y = list(y1) + list(y2)

			sinal += list(y)

		elif sequencia[b] == '1':
			
			if sinal[-1] == 1: y = [-1] * taxa_amostragem * 2
			else: y = [1] * taxa_amostragem * 2

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "bi-phase-s")

def delay_modulation(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	zeroDuplo = False

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

def dicode_nrz(janela_principal, caixa_de_texto):

	sequencia = caixa_de_texto.get()

	sinal = [1]

	for b in range(len(sequencia)):
		if sequencia[b] == '1':

			if sinal[-1] == 1:
				y = [-1.0] * taxa_amostragem * 2

			elif sinal[-1] == 0:

				if b == 0:
					y = [-1.0] * taxa_amostragem * 2

				elif sequencia[b-1] == '1':

					y = [0] * taxa_amostragem * 2

				elif sequencia[b-1] == '0':

					y = [-1] * taxa_amostragem * 2

			elif sinal[-1] == -1:
				if b == 0:
					y = [-1.0] * taxa_amostragem * 2

				else:
					y = [0] * taxa_amostragem * 2

			sinal += list(y)

		elif sequencia[b] == '0':
			if sinal[-1] == -1:
				
				y = [1.0] * taxa_amostragem * 2

			elif sinal[-1] == 0:

				if b == 0:
					y = [1.0] * taxa_amostragem * 2

				elif sequencia[b-1] == '0':

					y = [0] * taxa_amostragem * 2

				elif sequencia[b-1] == '1':

					y = [1] * taxa_amostragem * 2

			elif sinal[-1] == 1:
				if b == 0:
					y = [1.0] * taxa_amostragem * 2

				else:
					y = [0] * taxa_amostragem * 2

			sinal += list(y)

	y = sinal
	x = np.linspace(0.0, len(sequencia), len(y))

	desenha_grafico(x, y, sequencia, "dicode nrz")



def menu(janela_principal):
	

	label_digitar_sequencia = Label(janela_principal, text="Digite a sequência de 16 bits:", font=14, bg='white')
	label_digitar_sequencia.place(x=10, y=10)

	caixa_de_texto = Entry(janela_principal, width=16, font=14, bg='#DDD')
	caixa_de_texto.place(x=10, y=40)

	label_digitar_sequencia = Label(janela_principal, text="Escolha o tipo do PCM:", font=14, bg='white')
	label_digitar_sequencia.place(x=10, y=70)

	y = 100
	botao_nrz_l = Button(janela_principal, width=16, font=None, text="NRZ-L")
	botao_nrz_l.place(x=10, y=y)

	y+=30
	botao_nrz_m = Button(janela_principal, width=16, font=None, text="NRZ-M")
	botao_nrz_m.place(x=10, y=y)

	y+=30
	botao_nrz_s = Button(janela_principal, width=16, font=None, text="NRZ-S")
	botao_nrz_s.place(x=10, y=y)

	y+=30
	botao_unipolar_rz = Button(janela_principal, width=16, font=None, text="Unipolar RZ")
	botao_unipolar_rz.place(x=10, y=y)

	y+=30
	botao_bipolar_rz = Button(janela_principal, width=16, font=None, text="Bipolar RZ")
	botao_bipolar_rz.place(x=10, y=y)

	y+=30
	botao_rz_ami = Button(janela_principal, width=16, font=None, text="RZ-AMI")
	botao_rz_ami.place(x=10, y=y)

	y+=30
	botao_bi_phase_l = Button(janela_principal, width=16, font=None, text="Bi-PHASE-L")
	botao_bi_phase_l.place(x=10, y=y)

	y+=30
	botao_bi_phase_m = Button(janela_principal, width=16, font=None, text="Bi-PHASE-M")
	botao_bi_phase_m.place(x=10, y=y)

	y+=30
	botao_bi_phase_s = Button(janela_principal, width=16, font=None, text="Bi-PHASE-S")
	botao_bi_phase_s.place(x=10, y=y)

	y+=30
	botao_delay_modulation = Button(janela_principal, width=16, font=None, text="Delay Modulation")
	botao_delay_modulation.place(x=10, y=y)

	y+=30
	botao_delay_dicode_nrz = Button(janela_principal, width=16, font=None, text="Dicode NRZ")
	botao_delay_dicode_nrz.place(x=10, y=y)
	

	botao_nrz_l["command"] = partial(nrz_l, janela_principal, caixa_de_texto)
	botao_nrz_m["command"] = partial(nrz_m, janela_principal, caixa_de_texto)
	botao_nrz_s["command"] = partial(nrz_s, janela_principal, caixa_de_texto)
	botao_unipolar_rz["command"] = partial(unipolar_rz, janela_principal, caixa_de_texto)
	botao_bipolar_rz["command"] = partial(bipolar_rz, janela_principal, caixa_de_texto)
	botao_rz_ami["command"] = partial(rz_ami, janela_principal, caixa_de_texto)
	botao_bi_phase_l["command"] = partial(bi_phase_l, janela_principal, caixa_de_texto)
	botao_bi_phase_m["command"] = partial(bi_phase_m, janela_principal, caixa_de_texto)
	botao_bi_phase_s["command"] = partial(bi_phase_s, janela_principal, caixa_de_texto)
	botao_delay_modulation["command"] = partial(delay_modulation, janela_principal, caixa_de_texto)
	botao_delay_dicode_nrz["command"] = partial(dicode_nrz, janela_principal, caixa_de_texto)

	
menu(janela_principal)

janela_principal.geometry("{0}x{1}+0+0".format(janela_principal.winfo_screenwidth(), janela_principal.winfo_screenheight()))
janela_principal.mainloop()