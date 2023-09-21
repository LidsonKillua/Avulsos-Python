"""
Este código utiliza os dados de produtos, estoque e vendas da loja LAURA SMART
para gerar dois relatórios, um com as informações de vendas e outro com as
informações de clientes.
"""

"""
    QUADRO 1 – Itens comercializados pela LAURA SMART
    Descrição dos Itens Estoque (ud) Preços (R$/ud)
    Kit Arduino Iniciante 317 149,90
    Kit Arduino Robótica 291 415,90
    Kit Automação Residência 280 199,90
    Placa Arduino Nano 494 56,90
    Placa Arduino UNO 1080 74,90
    Placa Raspberry 326 699,00
"""

Produtos = ["Kit Arduino Iniciante", "Kit Arduino Robótica", "Kit Automação Residência",
            "Placa Arduino Nano", "Placa Arduino UNO", "Placa Raspberry"]

# Cada índice i da lista representa um item ex lista[0][i] = Quantidade, lista[1][i] = Preço
Estoque = [[317, 291, 280, 494, 1080, 326],
           [149.90, 415.90, 199.90, 56.90, 74.90, 699.00]]

"""
UNIOPA 24 32 23 45 120 23
UFRT 35 12 56 78 135 45
UFVIM 23 16 12 60 154 78
UNIMOR 120 18 90 52 190 37
UFLAR 50 130 32 56 167 54
UFTTI 12 34 20 120 134 34
"""

# Cada índice i da lista representa uma empresa ex lista[i][j] = UNIOPA, lista[i][j] = UFRT
# e cada índice j da lista representa um produto ex lista[i][j = 0] = Arduino iniciante
Vendas = [[24, 32, 23, 45, 120, 23],
          [35, 12, 56, 78, 135, 45],
          [23, 16, 12, 60, 154, 78],
          [120, 18, 90, 52, 190, 37],
          [50, 130, 32, 56, 167, 54],
          [12, 34, 20, 120, 134, 34]]

QtdTotalVendido = [0, 0, 0, 0, 0, 0]
Faturamento = [0, 0, 0, 0, 0, 0]

Clientes = ['UNIOPA', 'UFRT', 'UFVIM', 'UNIMOR', 'UFLAR', 'UFTTI']
QtdClientes = 6
Gastos = [0, 0, 0, 0, 0, 0]

# Calcular a quantidade total vendida e o faturamento de cada item  e o gasto de cada cliente
for i in range(len(Vendas)):
    for j in range(len(Produtos)):
        QtdTotalVendido[j] += Vendas[i][j]
        Faturamento[j] += Vendas[i][j] * Estoque[1][j]
        Gastos[i] += Vendas[i][j] * Estoque[1][j]

# Calcula o faturamento total e o maior faturamento
TotalFaturamento = 0
MaiorFaturamento = 0
itemMaiorFaturamento = ''
for i in range(len(Faturamento)):
    TotalFaturamento += Faturamento[i]

    if Faturamento[i] > MaiorFaturamento:
        MaiorFaturamento = Faturamento[i]
        itemMaiorFaturamento = Produtos[i]

"""
Gerar “Relatório I - Vendas - LOJA LAURA SMART” no formato de tabela para
a análise dos gestores com as seguintes informações:
(a) quantidades totais vendidas de cada item;
(b) quantidades de cada item em estoque após as vendas;
(b) faturamento da venda de cada item;
(c) faturamento total na venda de todos os itens; e
(d) indicação do item que possibilitou maior faturamento.
"""
linha = '_' * 105

print(linha)
print('{:^80}'.format('Relatório I - Vendas - LOJA LAURA SMART'))
print(linha)

print('{:<27s}{:>10s}{:>15s}{:>15s}{:>15s}{:>20s}'.format("Produtos", "Vendido", "Estoque", 
                                                          "Faturamento", "Total", "Maior Fat."))

for i in range(len(Produtos)):
    print('{:<27s}{:>10d}{:>15d}{:>15.2f}{:>15.2f}{:>20s}'.format(Produtos[i], QtdTotalVendido[i], 
                                                                  Estoque[0][i] - QtdTotalVendido[i], 
                                                                  Faturamento[i], TotalFaturamento, itemMaiorFaturamento))

print(linha)
print()

"""
Gerar 'Relatório II - Clientes - LOJA LAURA SMART” no formato de tabela
apresentando as seguintes informações sobre os clientes:
(a) Gastos de cada um dos clientes;
(b) Indicação do cliente responsável pelo maior gasto;
(c) Cálculo do valor médio gasto pelos clientes; e
(d) Indicação do cliente responsável pelo menor gasto.
"""

# Calcular a média de gastos dos clientes
GastoTotal = 0
for i in range(len(Gastos)):
    GastoTotal += Gastos[i]

MediaGastos = GastoTotal / QtdClientes

# Calcular o maior e menor gasto
MaiorGasto = 0
MenorGasto = 0
ClienteMaiorGasto = ''
ClienteMenorGasto = ''
for i in range(len(Gastos)):
    if Gastos[i] > MaiorGasto:
        MaiorGasto = Gastos[i]
        ClienteMaiorGasto = Clientes[i]

    if Gastos[i] < MenorGasto:
        MenorGasto = Gastos[i]
        ClienteMenorGasto = Clientes[i]

linha = '_' * 105

print(linha)
print('{:^80}'.format('Relatório II - Clientes - LOJA LAURA SMART'))
print(linha)


print('{:<20s}{:>15s}{:>15s}{:>15s}{:>15s}'.format("Clientes", "Gastos", "Maior Gasto", "Média Gastos", "Menor Gasto"))

for i in range(len(Clientes)):
    print('{:<20s}{:>15.2f}{:>15s}{:>15.2f}{:>15s}'.format(Clientes[i], Gastos[i], ClienteMaiorGasto, 
                                                           MediaGastos, ClienteMenorGasto))

print(linha)
