from tkinter import *
from tkinter import ttk


# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

janela = Tk()
janela.title("Calculadora de Resistor")
janela.geometry("850x650")
janela.resizable(False, False)
janela.configure(bg="#f2f2f2")


# ==========================================================
# TABELAS
# ==========================================================

# Valores das cores
valores_cores = {
    "preto": 0,
    "marrom": 1,
    "vermelho": 2,
    "laranja": 3,
    "amarelo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "cinza": 8,
    "branco": 9
}

# Cores usadas pelo Tkinter
cores_tkinter = {
    "preto": "black",
    "marrom": "#8B4513",
    "vermelho": "#E53935",
    "laranja": "#FF8C00",
    "amarelo": "#FFD700",
    "verde": "#2E8B57",
    "azul": "#1976D2",
    "violeta": "#8E44AD",
    "cinza": "#808080",
    "branco": "white",
    "ouro": "#D4AF37",
    "prata": "#C0C0C0"
}

# Multiplicadores
multiplicadores = {
    "preto": 1,
    "marrom": 10,
    "vermelho": 100,
    "laranja": 1000,
    "amarelo": 10000,
    "verde": 100000,
    "azul": 1000000,
    "violeta": 10000000,
    "cinza": 100000000,
    "branco": 1000000000,
    "ouro": 0.1,
    "prata": 0.01
}

# Tolerâncias
tolerancias = {
    "marrom": 1,
    "vermelho": 2,
    "verde": 0.5,
    "azul": 0.25,
    "violeta": 0.1,
    "cinza": 0.05,
    "ouro": 5,
    "prata": 10
}

# Cores permitidas para as duas primeiras bandas
cores_bandas = list(valores_cores.keys())

# Cores permitidas para multiplicador
cores_multiplicador = list(multiplicadores.keys())

# Cores permitidas para tolerância
cores_tolerancia = list(tolerancias.keys())


# ==========================================================
# FUNÇÕES
# ==========================================================

def formatar_resistencia(valor):
    """
    Converte o valor para uma unidade mais fácil de ler.
    """

    if valor >= 1000000000:
        return f"{valor / 1000000000:g} GΩ"

    elif valor >= 1000000:
        return f"{valor / 1000000:g} MΩ"

    elif valor >= 1000:
        return f"{valor / 1000:g} kΩ"

    else:
        return f"{valor:g} Ω"


def limpar():
    """
    Limpa os campos e o resultado.
    """

    entrada_valor.delete(0, END)

    banda1.set("vermelho")
    banda2.set("vermelho")
    multiplicador.set("laranja")
    tolerancia.set("ouro")

    texto_resultado.config(
        text="Resultado aparecerá aqui.",
        fg="#222222"
    )

    canvas.delete("all")


def calcular_por_cores():
    """
    Calcula a resistência utilizando as quatro bandas.
    """

    b1 = banda1.get()
    b2 = banda2.get()
    mult = multiplicador.get()
    tol = tolerancia.get()

    # Obtém os valores das duas primeiras bandas
    valor1 = valores_cores[b1]
    valor2 = valores_cores[b2]

    # Junta os dois valores
    numero = valor1 * 10 + valor2

    # Aplica o multiplicador
    resistencia = numero * multiplicadores[mult]

    # Obtém a tolerância
    tolerancia_valor = tolerancias[tol]

    # Formata o resultado
    resultado = formatar_resistencia(resistencia)

    # Calcula os limites
    minimo = resistencia * (1 - tolerancia_valor / 100)
    maximo = resistencia * (1 + tolerancia_valor / 100)

    # Mostra resultado
    texto_resultado.config(
        text=(
            f"Resistência: {resultado}\n"
            f"Tolerância: ±{tolerancia_valor}%\n"
            f"Faixa: {formatar_resistencia(minimo)} até "
            f"{formatar_resistencia(maximo)}"
        ),
        fg="#222222"
    )

    # Desenha o resistor
    desenhar_resistor(
        cores_tkinter[b1],
        cores_tkinter[b2],
        cores_tkinter[mult],
        cores_tkinter[tol]
    )


def calcular_por_valor():
    """
    Tenta encontrar as cores correspondentes
    ao valor informado.
    """

    entrada = entrada_valor.get().replace(",", ".")

    try:
        valor = float(entrada)

        if valor <= 0:
            raise ValueError

    except ValueError:
        texto_resultado.config(
            text="Digite um valor válido. Exemplo: 2200",
            fg="red"
        )
        return

    encontrado = False

    # Percorre as possíveis combinações
    for b1_nome, b1_valor in valores_cores.items():

        for b2_nome, b2_valor in valores_cores.items():

            numero = b1_valor * 10 + b2_valor

            for mult_nome, mult_valor in multiplicadores.items():

                resultado = numero * mult_valor

                if resultado == valor:

                    texto_resultado.config(
                        text=(
                            f"Resistência: {formatar_resistencia(valor)}\n"
                            f"Cores: {b1_nome}, {b2_nome}, "
                            f"{mult_nome}, ouro\n"
                            f"Tolerância: ±5%"
                        ),
                        fg="#222222"
                    )

                    desenhar_resistor(
                        cores_tkinter[b1_nome],
                        cores_tkinter[b2_nome],
                        cores_tkinter[mult_nome],
                        cores_tkinter["ouro"]
                    )

                    encontrado = True
                    return

    if not encontrado:
        texto_resultado.config(
            text=(
                "Não foi possível encontrar uma combinação "
                "de 4 bandas para esse valor."
            ),
            fg="red"
        )

    canvas.delete("all")


def calcular():
    """
    Decide qual cálculo será executado
    dependendo do modo selecionado.
    """

    if opcao.get() == "cores":
        calcular_por_cores()

    else:
        calcular_por_valor()


def desenhar_resistor(cor1, cor2, cor3, cor4):
    """
    Desenha um resistor utilizando o Canvas.
    """

    canvas.delete("all")

    # Fio esquerdo
    canvas.create_line(
        80, 125,
        220, 125,
        width=5
    )

    # Fio direito
    canvas.create_line(
        580, 125,
        720, 125,
        width=5
    )

    # Corpo do resistor
    canvas.create_rectangle(
        220, 80,
        580, 170,
        fill="#D2A679",
        outline="#333333",
        width=2
    )

    # Faixa 1
    canvas.create_rectangle(
        270, 80,
        305, 170,
        fill=cor1,
        outline=""
    )

    # Faixa 2
    canvas.create_rectangle(
        330, 80,
        365, 170,
        fill=cor2,
        outline=""
    )

    # Faixa 3
    canvas.create_rectangle(
        390, 80,
        425, 170,
        fill=cor3,
        outline=""
    )

    # Faixa 4 - tolerância
    canvas.create_rectangle(
        510, 80,
        545, 170,
        fill=cor4,
        outline=""
    )


def mudar_modo():
    """
    Alterna entre:
    Cores -> Valor
    Valor -> Cores
    """

    if opcao.get() == "cores":

        frame_bandas.pack(pady=15)
        frame_valor.pack_forget()

    else:

        frame_bandas.pack_forget()
        frame_valor.pack(pady=15)


# ==========================================================
# TÍTULO
# ==========================================================

titulo = Label(
    janela,
    text="CALCULADORA DE RESISTOR",
    font=("Arial", 20, "bold"),
    bg="#f2f2f2",
    fg="#222222"
)

titulo.pack(pady=(20, 5))


subtitulo = Label(
    janela,
    text="Descubra o valor de um resistor através das cores",
    font=("Arial", 11),
    bg="#f2f2f2",
    fg="#666666"
)

subtitulo.pack()


# ==========================================================
# ESCOLHA DO MODO
# ==========================================================

frame_modo = Frame(
    janela,
    bg="#f2f2f2"
)

frame_modo.pack(pady=20)

Label(
    frame_modo,
    text="Modo:",
    font=("Arial", 11, "bold"),
    bg="#f2f2f2"
).pack(side=LEFT, padx=5)

opcao = StringVar(value="cores")

Radiobutton(
    frame_modo,
    text="Cores → Valor",
    variable=opcao,
    value="cores",
    command=mudar_modo,
    bg="#f2f2f2"
).pack(side=LEFT, padx=10)

Radiobutton(
    frame_modo,
    text="Valor → Cores",
    variable=opcao,
    value="valor",
    command=mudar_modo,
    bg="#f2f2f2"
).pack(side=LEFT, padx=10)


# ==========================================================
# FRAME DAS BANDAS
# ==========================================================

frame_bandas = Frame(
    janela,
    bg="#f2f2f2"
)

frame_bandas.pack(pady=15)


# ---------------- BANDA 1 ----------------

Label(
    frame_bandas,
    text="Banda 1",
    font=("Arial", 10, "bold"),
    bg="#f2f2f2"
).grid(row=0, column=0, padx=8)

banda1 = ttk.Combobox(
    frame_bandas,
    values=cores_bandas,
    width=13,
    state="readonly"
)

banda1.set("vermelho")

banda1.grid(
    row=1,
    column=0,
    padx=8
)


# ---------------- BANDA 2 ----------------

Label(
    frame_bandas,
    text="Banda 2",
    font=("Arial", 10, "bold"),
    bg="#f2f2f2"
).grid(row=0, column=1, padx=8)

banda2 = ttk.Combobox(
    frame_bandas,
    values=cores_bandas,
    width=13,
    state="readonly"
)

banda2.set("vermelho")

banda2.grid(
    row=1,
    column=1,
    padx=8
)


# ---------------- MULTIPLICADOR ----------------

Label(
    frame_bandas,
    text="Multiplicador",
    font=("Arial", 10, "bold"),
    bg="#f2f2f2"
).grid(row=0, column=2, padx=8)

multiplicador = ttk.Combobox(
    frame_bandas,
    values=cores_multiplicador,
    width=13,
    state="readonly"
)

multiplicador.set("laranja")

multiplicador.grid(
    row=1,
    column=2,
    padx=8
)


# ---------------- TOLERÂNCIA ----------------

Label(
    frame_bandas,
    text="Tolerância",
    font=("Arial", 10, "bold"),
    bg="#f2f2f2"
).grid(row=0, column=3, padx=8)

tolerancia = ttk.Combobox(
    frame_bandas,
    values=cores_tolerancia,
    width=13,
    state="readonly"
)

tolerancia.set("ouro")

tolerancia.grid(
    row=1,
    column=3,
    padx=8
)


# ==========================================================
# FRAME DO VALOR
# ==========================================================

frame_valor = Frame(
    janela,
    bg="#f2f2f2"
)

Label(
    frame_valor,
    text="Digite o valor da resistência:",
    font=("Arial", 11, "bold"),
    bg="#f2f2f2"
).pack(side=LEFT, padx=5)

entrada_valor = Entry(
    frame_valor,
    width=20,
    font=("Arial", 11)
)

entrada_valor.pack(side=LEFT, padx=5)

Label(
    frame_valor,
    text="Ω",
    font=("Arial", 11, "bold"),
    bg="#f2f2f2"
).pack(side=LEFT)


# Inicialmente escondido
frame_valor.pack_forget()


# ==========================================================
# BOTÕES
# ==========================================================

frame_botoes = Frame(
    janela,
    bg="#f2f2f2"
)

frame_botoes.pack(pady=5)


Button(
    frame_botoes,
    text="CALCULAR",
    font=("Arial", 11, "bold"),
    bg="#90EE90",
    width=18,
    command=calcular
).pack(side=LEFT, padx=5)


Button(
    frame_botoes,
    text="LIMPAR",
    font=("Arial", 11),
    bg="#FFB6B6",
    width=12,
    command=limpar
).pack(side=LEFT, padx=5)


# ==========================================================
# RESULTADO
# ==========================================================

Label(
    janela,
    text="RESULTADO",
    font=("Arial", 12, "bold"),
    bg="#f2f2f2"
).pack(pady=(15, 5))


texto_resultado = Label(
    janela,
    text="Resultado aparecerá aqui.",
    font=("Arial", 13),
    bg="white",
    width=70,
    height=4,
    relief="solid",
    borderwidth=1,
    justify=LEFT,
    anchor="w"
)

texto_resultado.pack(pady=5)


# ==========================================================
# CANVAS
# ==========================================================

canvas = Canvas(
    janela,
    width=800,
    height=220,
    bg="white",
    highlightthickness=1,
    highlightbackground="#cccccc"
)

canvas.pack(pady=15)


# ==========================================================
# INICIAR
# ==========================================================

janela.mainloop()
