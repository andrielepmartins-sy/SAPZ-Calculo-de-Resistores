from tkinter import StringVar, Tk, Canvas, Label, Radiobutton, Frame, Button, ttk

janela = Tk()

janela.geometry("800x600")
janela.title("Calculadora de Resistor")


# ---------------- TÍTULO ----------------

titulo = Label(
    janela,
    text="Calculadora de Resistor",
    fg="black",
    font=("Arial", 15)
)

titulo.pack(pady=10, anchor="w", padx=10)


# ---------------- TEXTO ----------------

texto = Label(
    janela,
    text="Como deseja informar o resistor?",
    fg="black",
    bg="silver",
    font=("Arial", 15)
)

texto.pack(pady=5, anchor="w", padx=40)


# ---------------- OPÇÕES ----------------

frame_opcoes = Frame(janela)
frame_opcoes.pack(anchor="w", padx=40, pady=5)

opcao = StringVar()
opcao.set("cores")

Radiobutton(
    frame_opcoes,
    bg="lightgray",
    text="Valor da resistência",
    variable=opcao,
    value="valor"
).pack(side="left", padx=2)

Radiobutton(
    frame_opcoes,
    bg="lightgray",
    text="Cores do resistor",
    variable=opcao,
    value="cores"
).pack(side="left", padx=10)


# ---------------- BANDAS DO RESISTOR ----------------

frame_bandas = Frame(janela)
frame_bandas.pack(pady=20)


# Banda 1

Label(
    frame_bandas,
    text="Banda 1:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, sticky="w")

banda1 = ttk.Combobox(
    frame_bandas,
    values=[
        "vermelho", "laranja", "amarelo",
        "verde", "azul", "violeta",
        "cinza", "branco"
    ],
    width=15
)

banda1.set("vermelho")
banda1.grid(row=1, column=0, padx=10)


# Banda 2

Label(
    frame_bandas,
    text="Banda 2:",
    font=("Arial", 12)
).grid(row=0, column=1, padx=10, sticky="w")

banda2 = ttk.Combobox(
    frame_bandas,
    values=[
        "vermelho", "laranja", "amarelo",
        "verde", "azul", "violeta",
        "cinza", "branco"
    ],
    width=15
)

banda2.set("vermelho")
banda2.grid(row=1, column=1, padx=10)


# Multiplicador

Label(
    frame_bandas,
    text="Multiplicador:",
    font=("Arial", 12)
).grid(row=0, column=2, padx=10, sticky="w")

multiplicador = ttk.Combobox(
    frame_bandas,
    values=[
        "laranja", "amarelo", "verde",
        "azul", "violeta", "cinza",
        "branco", "prata", "ouro"
    ],
    width=15
)

multiplicador.set("laranja")
multiplicador.grid(row=1, column=2, padx=10)


# Tolerância

Label(
    frame_bandas,
    text="Tolerância:",
    font=("Arial", 12)
).grid(row=0, column=3, padx=10, sticky="w")

tolerancia = ttk.Combobox(
    frame_bandas,
    values=["violeta", "cinza", "prata", "ouro"],
    width=15
)

tolerancia.set("violeta")
tolerancia.grid(row=1, column=3, padx=10)


# ---------------- FUNÇÃO CALCULAR ----------------

def calcular_resistor():

    b1 = banda1.get()
    b2 = banda2.get()
    m = multiplicador.get()
    t = tolerancia.get()

    texto_resultado.config(
        text=f"Resistência: {b1}, {b2}, {m}, {t}"
    )


# ---------------- BOTÃO CALCULAR ----------------

button_frame = Frame(janela)
button_frame.pack(anchor="w", padx=40, pady=10)

botao_calcular = Button(
    button_frame,
    text="Calcular Resistência",
    bg="lightgreen",
    font=("Arial", 11),
    command=calcular_resistor
)

botao_calcular.pack()


# ---------------- RESULTADO ---------------------

texto_resultado = Label(
    janela,
    text="Resistência:",
    fg="black",
    font=("Arial", 15)
)

texto_resultado.pack(
    anchor="w",
    padx=40,
    pady=10
)


# ---------------- CANVAS ----------------

canvas = Canvas(
    janela,
    width=700,
    height=250
)

canvas.pack()


janela.mainloop()