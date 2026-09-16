from tkinter import *
from tkinter import ttk

from configuracoes import janela
from tabelas import cores_bandas, cores_multiplicador, cores_tolerancia
from calculos import calcular
from desenho import desenhar_resistor


def criar_interface():
    global entrada_valor, banda1, banda2, multiplicador, tolerancia
    global tolerancia_valor, texto_resultado, canvas, botao_calcular
    global frame_valor, frame_bandas, opcao

    # ==========================================================
    # TÍTULO
    # ==========================================================

    titulo = Label(
        janela,
        text="Calculadora de Resistor",
        font=("Arial", 18, "bold"),
        bg="#eef2f5",
        fg="#263238"
    )

    titulo.pack(
        anchor="w",
        padx=20,
        pady=(15, 7)
    )

    # ==========================================================
    # PAINEL
    # ==========================================================

    painel = Frame(
        janela,
        bg="white"
    )

    painel.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )

    # ==========================================================
    # MODO
    # ==========================================================

    Label(
        painel,
        text="Como deseja informar o resistor?",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#263238"
    ).pack(
        anchor="w",
        padx=15,
        pady=(12, 2)
    )

    opcao = StringVar(value="cores")

    frame_opcoes = Frame(
        painel,
        bg="white"
    )

    frame_opcoes.pack(
        anchor="w",
        padx=10
    )

    # ==========================================================
    # CONTEÚDO FIXO
    # ==========================================================

    frame_conteudo = Frame(
        painel,
        bg="white",
        height=55
    )

    frame_conteudo.pack(
        fill="x",
        padx=15,
        pady=(7, 3)
    )

    frame_conteudo.pack_propagate(False)

    # ==========================================================
    # BANDAS
    # ==========================================================

    frame_bandas = Frame(
        frame_conteudo,
        bg="white"
    )

    frame_bandas.pack(
        fill="x"
    )

    Label(
        frame_bandas,
        text="Banda 1:",
        font=("Arial", 9),
        bg="white"
    ).grid(row=0, column=0, sticky="w")

    banda1 = ttk.Combobox(
        frame_bandas,
        values=cores_bandas,
        width=11,
        state="readonly"
    )

    banda1.set("vermelho")

    banda1.grid(
        row=1,
        column=0,
        padx=(0, 7)
    )

    Label(
        frame_bandas,
        text="Banda 2:",
        font=("Arial", 9),
        bg="white"
    ).grid(row=0, column=1, sticky="w")

    banda2 = ttk.Combobox(
        frame_bandas,
        values=cores_bandas,
        width=11,
        state="readonly"
    )

    banda2.set("vermelho")

    banda2.grid(
        row=1,
        column=1,
        padx=7
    )

    Label(
        frame_bandas,
        text="Multiplicador:",
        font=("Arial", 9),
        bg="white"
    ).grid(row=0, column=2, sticky="w")

    multiplicador = ttk.Combobox(
        frame_bandas,
        values=cores_multiplicador,
        width=11,
        state="readonly"
    )

    multiplicador.set("laranja")

    multiplicador.grid(
        row=1,
        column=2,
        padx=7
    )

    Label(
        frame_bandas,
        text="Tolerância:",
        font=("Arial", 9),
        bg="white"
    ).grid(row=0, column=3, sticky="w")

    tolerancia = ttk.Combobox(
        frame_bandas,
        values=cores_tolerancia,
        width=11,
        state="readonly"
    )

    tolerancia.set("ouro")

    tolerancia.grid(
        row=1,
        column=3,
        padx=(7, 0)
    )

    # ==========================================================
    # VALOR DA RESISTÊNCIA
    # ==========================================================

    frame_valor = Frame(
        frame_conteudo,
        bg="white"
    )

    Label(
        frame_valor,
        text="Valor (Ω):",
        font=("Arial", 9),
        bg="white"
    ).pack(side=LEFT)

    entrada_valor = Entry(
        frame_valor,
        width=18,
        font=("Arial", 10)
    )

    entrada_valor.pack(
        side=LEFT,
        padx=6
    )

    Label(
        frame_valor,
        text="Tolerância:",
        font=("Arial", 9),
        bg="white"
    ).pack(
        side=LEFT,
        padx=(8, 5)
    )

    tolerancia_valor = ttk.Combobox(
        frame_valor,
        values=cores_tolerancia,
        width=10,
        state="readonly"
    )

    tolerancia_valor.set("ouro")

    tolerancia_valor.pack(side=LEFT)

    # ==========================================================
    # BOTÕES
    # ==========================================================

    frame_botoes = Frame(
        painel,
        bg="white"
    )

    frame_botoes.pack(
        anchor="w",
        padx=15,
        pady=5
    )

    def executar_calculo():
        calcular(
            opcao,
            banda1,
            banda2,
            multiplicador,
            tolerancia,
            entrada_valor,
            tolerancia_valor,
            texto_resultado,
            canvas
        )

    def limpar():
        entrada_valor.delete(0, END)

        banda1.set("vermelho")
        banda2.set("vermelho")
        multiplicador.set("laranja")
        tolerancia.set("ouro")
        tolerancia_valor.set("ouro")

        texto_resultado.config(
            text="Selecione as cores ou informe um valor.",
            fg="#666666"
        )

        canvas.delete("all")

    def mudar_modo():
        if opcao.get() == "cores":
            frame_valor.pack_forget()

            frame_bandas.pack(
                fill="x"
            )

            botao_calcular.config(
                text="Calcular resistência"
            )

        else:
            frame_bandas.pack_forget()

            frame_valor.pack(
                fill="x"
            )

            botao_calcular.config(
                text="Calcular cores"
            )

        entrada_valor.delete(0, END)

        texto_resultado.config(
            text="Selecione as cores ou informe um valor.",
            fg="#666666"
        )

        canvas.delete("all")

    Radiobutton(
        frame_opcoes,
        text="Cores do resistor",
        variable=opcao,
        value="cores",
        command=mudar_modo,
        bg="white",
        activebackground="white"
    ).pack(side=LEFT)

    Radiobutton(
        frame_opcoes,
        text="Valor da resistência",
        variable=opcao,
        value="valor",
        command=mudar_modo,
        bg="white",
        activebackground="white"
    ).pack(
        side=LEFT,
        padx=15
    )

    botao_calcular = Button(
        frame_botoes,
        text="Calcular resistência",
        font=("Arial", 10, "bold"),
        bg="#4FAEA4",
        fg="white",
        activebackground="#438F87",
        activeforeground="white",
        relief="flat",
        padx=8,
        pady=5,
        command=executar_calculo
    )

    botao_calcular.pack(side=LEFT)

    Button(
        frame_botoes,
        text="Limpar",
        font=("Arial", 10),
        bg="#dddddd",
        relief="flat",
        padx=10,
        pady=5,
        command=limpar
    ).pack(
        side=LEFT,
        padx=7
    )

    # ==========================================================
    # RESULTADO
    # ==========================================================

    Label(
        painel,
        text="Resultado",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#263238"
    ).pack(
        anchor="w",
        padx=15,
        pady=(2, 3)
    )

    texto_resultado = Label(
        painel,
        text="Selecione as cores ou informe um valor.",
        font=("Arial", 10),
        bg="#f5f7f9",
        fg="#666666",
        relief="solid",
        bd=1,
        anchor="w",
        padx=8
    )

    texto_resultado.pack(
        fill="x",
        padx=15,
        ipady=6
    )

    # ==========================================================
    # RESISTOR
    # ==========================================================

    canvas = Canvas(
        painel,
        width=525,
        height=145,
        bg="#f8fafc",
        highlightthickness=1,
        highlightbackground="#d5dce3"
    )

    canvas.pack(
        padx=15,
        pady=7
    )
