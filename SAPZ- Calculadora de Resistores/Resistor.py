from tkinter import Tk, Canvas, Label

janela = Tk()

janela.geometry("500x450")
janela.title("Calculadora de Resistor")

# ---------------- TÍTULO ----------------

titulo = Label(
    janela,
    text="Calculadora de Resistor",
    fg="black",
    font=("Arial", 15)
)

titulo.pack(pady=10, anchor="w")

# ---------------- CANVAS ----------------

canvas = Canvas(
    janela,
    width=400,
    height=800
)

# ---------------- BASE DO RESISTOR -------------------

canvas.create_rectangle(
    40, 300,
    300, 350,
    fill="tan"
)

# ---------------- LINHA ------------------------------

canvas.create_line(
    5, 325,
    40, 325,
    fill="gray",
    width=3
)

canvas.create_line(
    300, 325,
    340, 325,
    fill="gray",
    width=3
)

canvas.pack()

janela.mainloop()