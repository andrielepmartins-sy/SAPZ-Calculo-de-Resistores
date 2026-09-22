def formatar_resistencia(valor):

    if valor >= 1000000000:
        return f"{valor / 1000000000:g} GΩ"

    elif valor >= 1000000:
        return f"{valor / 1000000:g} MΩ"

    elif valor >= 1000:
        return f"{valor / 1000:g} kΩ"

    else:
        return f"{valor:g} Ω"