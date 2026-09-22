# SAPZ - Calculadora de Resistores

Projeto desenvolvido em **Python com Tkinter** para calcular valores de resistores a partir do código de cores e também identificar as cores correspondentes a partir do valor da resistência.

## Sobre o projeto

Os resistores possuem faixas coloridas que representam seu valor de resistência e sua tolerância. A proposta deste projeto é facilitar a identificação desses valores por meio de uma aplicação gráfica.

A aplicação permite trabalhar de duas formas:

* Informar as cores do resistor e obter seu valor.
* Informar o valor da resistência e descobrir as cores correspondentes.

Além do cálculo, o programa possui uma representação visual do resistor, permitindo visualizar as faixas de cores selecionadas.

## Funcionalidades

### Cores do resistor → Valor

O usuário seleciona:

* Banda 1
* Banda 2
* Multiplicador
* Tolerância

Após clicar em **"Calcular Resistência"**, o sistema apresenta o valor da resistência utilizando a unidade adequada:

* Ω
* kΩ
* MΩ
* GΩ

Exemplo:

```text
Vermelho + Vermelho + Laranja + Violeta

22 kΩ ±0,1%
```

### Valor → Cores do resistor

O usuário informa o valor da resistência e o sistema identifica as faixas de cores correspondentes.

Exemplo:

```text
Valor informado:

22000 Ω

Resultado:

Vermelho + Vermelho + Laranja
```

### Representação visual

O programa também apresenta um desenho do resistor com as faixas de cores selecionadas, permitindo visualizar o resultado de forma gráfica.

## Tecnologias utilizadas

* **Python 3**
* **Tkinter**
* Programação Orientada a Objetos
* Git e GitHub

## Estrutura do projeto

```text
SAPZ- Calculadora de Resistores/
│
├── main.py
├── interface.py
├── configuracoes.py
├── calculos.py
├── tabelas.py
├── funcoes.py
├── desenho.py
├── Resistor.py
└── .gitignore
```

### Descrição dos arquivos

| Arquivo            | Função                                                     |
| ------------------ | ---------------------------------------------------------- |
| `main.py`          | Arquivo principal responsável por iniciar o programa       |
| `interface.py`     | Cria e organiza a interface gráfica                        |
| `configuracoes.py` | Contém as configurações da janela                          |
| `calculos.py`      | Realiza os cálculos dos valores dos resistores             |
| `tabelas.py`       | Contém os valores das cores, multiplicadores e tolerâncias |
| `funcoes.py`       | Possui funções auxiliares para o funcionamento do programa |
| `desenho.py`       | Responsável pelo desenho visual do resistor                |
| `Resistor.py`      | Contém a estrutura relacionada ao resistor                 |
| `.gitignore`       | Define arquivos que não devem ser enviados ao Git          |

## Como executar

### Pré-requisitos

É necessário ter o **Python 3** instalado no computador.

Para verificar a instalação, abra o terminal e execute:

```bash
python --version
```

Caso o comando acima não funcione, tente:

```bash
python3 --version
```

O projeto utiliza o **Tkinter** para criar a interface gráfica.

### Executando pelo terminal

1. Clone este repositório ou baixe os arquivos do projeto.

2. Abra o terminal dentro da pasta do projeto.

3. Execute o arquivo principal:

```bash
python main.py
```

No Linux ou macOS, caso necessário:

```bash
python3 main.py
```

A janela da **SAPZ - Calculadora de Resistores** será aberta.

### Executando pelo Visual Studio Code

Também é possível executar o projeto pelo **Visual Studio Code**:

1. Abra a pasta do projeto no VS Code.
2. Abra o arquivo `main.py`.
3. Clique no botão **Run Python File**.
4. A aplicação será iniciada.

## Objetivo do projeto

O projeto foi desenvolvido com o objetivo de aplicar conhecimentos de **programação em Python**, criação de **interfaces gráficas com Tkinter**, organização de código em diferentes arquivos e utilização de lógica para realizar cálculos relacionados a componentes eletrônicos.

## Autor

**Andriele Pinto Martins**

GitHub: [andrielepmartins-sy](https://github.com/andrielepmartins-sy)
