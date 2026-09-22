from configuracoes import janela

# ==========================================================
# TABELAS
# ==========================================================

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


cores_bandas = list(valores_cores.keys())
cores_multiplicador = list(multiplicadores.keys())
cores_tolerancia = list(tolerancias.keys())