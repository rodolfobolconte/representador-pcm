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