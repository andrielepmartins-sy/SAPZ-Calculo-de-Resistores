def desenhar_resistor(canvas, cor1, cor2, cor3, cor4):
    canvas.delete("all")

    # Fio esquerdo
    canvas.create_line(
        30, 70,
        120, 70,
        width=5,
        fill="#777777"
    )

    # Fio direito
    canvas.create_line(
        400, 70,
        490, 70,
        width=5,
        fill="#777777"
    )

    # Corpo do resistor
    canvas.create_rectangle(
        120, 35,
        400, 105,
        fill="#F0DFA6",
        outline="#555555",
        width=2
    )

    # Banda 1
    canvas.create_rectangle(
        165, 35,
        185, 105,
        fill=cor1,
        outline=""
    )

    # Banda 2
    canvas.create_rectangle(
        210, 35,
        230, 105,
        fill=cor2,
        outline=""
    )

    # Multiplicador
    canvas.create_rectangle(
        255, 35,
        275, 105,
        fill=cor3,
        outline=""
    )

    # Tolerância
    canvas.create_rectangle(
        335, 35,
        355, 105,
        fill=cor4,
        outline=""
    )