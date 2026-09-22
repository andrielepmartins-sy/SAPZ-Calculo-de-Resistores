from tabelas import valores_cores, multiplicadores, tolerancias, cores_tkinter
from funcoes import formatar_resistencia
from desenho import desenhar_resistor


def calcular_por_cores(banda1, banda2, multiplicador, tolerancia, texto_resultado, canvas):
    b1 = banda1.get()
    b2 = banda2.get()
    mult = multiplicador.get()
    tol = tolerancia.get()

    valor1 = valores_cores[b1]
    valor2 = valores_cores[b2]

    numero = valor1 * 10 + valor2
    resistencia = numero * multiplicadores[mult]
    tolerancia_valor = tolerancias[tol]
    resultado = formatar_resistencia(resistencia)

    texto_resultado.config(
        text=f"Resistência: {resultado} ±{tolerancia_valor}%",
        fg="#222222"
    )

    desenhar_resistor(
        canvas,
        cores_tkinter[b1],
        cores_tkinter[b2],
        cores_tkinter[mult],
        cores_tkinter[tol]
    )


def calcular_por_valor(entrada_valor, tolerancia_valor, texto_resultado, canvas, banda1, banda2, multiplicador, tolerancia):
    entrada = entrada_valor.get().replace(",", ".")

    try:
        valor = float(entrada)

        if valor <= 0:
            raise ValueError

    except ValueError:
        texto_resultado.config(
            text="Digite um valor válido.",
            fg="red"
        )

        canvas.delete("all")
        return

    for b1_nome, b1_valor in valores_cores.items():

        for b2_nome, b2_valor in valores_cores.items():

            numero = b1_valor * 10 + b2_valor

            for mult_nome, mult_valor in multiplicadores.items():

                resultado = numero * mult_valor

                if resultado == valor:
                    tol = tolerancia_valor.get()
                    tol_valor = tolerancias[tol]

                    texto_resultado.config(
                        text=(
                            f"Resistência: "
                            f"{formatar_resistencia(valor)} "
                            f"±{tol_valor}%"
                        ),
                        fg="#222222"
                    )

                    banda1.set(b1_nome)
                    banda2.set(b2_nome)
                    multiplicador.set(mult_nome)
                    tolerancia.set(tol)

                    desenhar_resistor(
                        canvas,
                        cores_tkinter[b1_nome],
                        cores_tkinter[b2_nome],
                        cores_tkinter[mult_nome],
                        cores_tkinter[tol]
                    )

                    return

    texto_resultado.config(
        text="Não foi encontrada uma combinação de 4 bandas.",
        fg="red"
    )

    canvas.delete("all")


def calcular(opcao, banda1, banda2, multiplicador, tolerancia, entrada_valor, tolerancia_valor, texto_resultado, canvas):
    if opcao.get() == "cores":
        calcular_por_cores(
            banda1, banda2, multiplicador, tolerancia,
            texto_resultado, canvas
        )
    else:
        calcular_por_valor(
            entrada_valor, tolerancia_valor, texto_resultado, canvas,
            banda1, banda2, multiplicador, tolerancia
        )