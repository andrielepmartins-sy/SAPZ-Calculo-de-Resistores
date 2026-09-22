# SAPZ - Calculadora de Resistores.

Projeto desenvolvido em Python com Tkinter para calcular valores de resistores a partir do código de cores e também identificar as cores correspondentes a partir do valor da resistência.

## Sobre o projeto

Os resistores possuem faixas coloridas que representam seu valor de resistência e sua tolerância. A proposta deste projeto é facilitar a identificação desses valores por meio de uma aplicação gráfica.

A aplicação permite trabalhar de duas formas:

- Informar as cores do resistor e obter seu valor.
- Informar o valor da resistência e descobrir as cores correspondentes.

Além do cálculo, o programa possui uma representação visual do resistor, permitindo visualizar as faixas de cores selecionadas.

## Funcionalidades

### Cores do resistor → Valor

O usuário seleciona:

- Banda 1
- Banda 2
- Multiplicador
- Tolerância

Após clicar em "Calcular Resistência", o sistema apresenta o valor da resistência utilizando a unidade adequada:

- Ω
- kΩ
- MΩ

Exemplo:

```text
Vermelho + Vermelho + Laranja + Violeta

22 kΩ ±0,1%

test 5.0

