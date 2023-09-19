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
TotalFaturamento = [0, 0, 0, 0, 0, 0]

Clientes = ['UNIOPA', 'UFRT', 'UFVIM', 'UNIMOR', 'UFLAR', 'UFTTI']
Gastos = [0, 0, 0, 0, 0, 0]

for i in range(len(Vendas)):
    for j in range(len(Produtos)):
        QtdTotalVendido[j] += Vendas[i][j]
        TotalFaturamento[j] += Vendas[i][j] * Estoque[1][j]
        Gastos[i] += Vendas[i][j] * Estoque[1][j]

"""
Gerar “Relatório I - Vendas - LOJA LAURA SMART” no formato de tabela para
a análise dos gestores com as seguintes informações:
(a) quantidades totais vendidas de cada item;
(b) quantidades de cada item em estoque após as vendas;
(b) faturamento da venda de cada item;
(c) faturamento total na venda de todos os itens; e
(d) indicação do item que possibilitou maior faturamento.
"""

""" Primeira Versão
print('Relatório I - Vendas - LOJA LAURA SMART')
for(i, produto) in enumerate(Produtos):
    print(f'{produto}:')
    print(f'Quantidade vendida: {QtdTotalVendido[i]}')
    print(f'Quantidade em estoque: {Estoque[0][i] - QtdTotalVendido[i]}')
    print(f'Faturamento: R$ {TotalFaturamento[i]:.2f}')
    print(f'Faturamento total: R$ {sum(TotalFaturamento):.2f}')
    print(f'Item que possibilitou maior faturamento: {Produtos[TotalFaturamento.index(max(TotalFaturamento))]}')
    print()
"""

print('Relatório I - Vendas - LOJA LAURA SMART')
str = 'Produtos: '
print(f'{str:25}', end="")
for produto in Produtos:
    print(f'{produto:>27}',end="")
print()

str = 'Quantidade vendida: '
print(f'{str:25}', end="")
for(i, produto) in enumerate(Produtos):
    print(f'{QtdTotalVendido[i]:27}', end="")
print()

str = 'Quantidade em estoque: '
print(f'{str:25}', end="")
for(i, produto) in enumerate(Produtos):
    print(f'{Estoque[0][i] - QtdTotalVendido[i]:27}', end="")
print()

str = 'Faturamento: '
print(f'{str:25}', end="")
for(i, produto) in enumerate(Produtos):
    val = 'R$ ' + f'{TotalFaturamento[i]:.2f}'
    print(f'{val:>27}', end="")
print()

str = 'Faturamento total: '
print(f'{str:25}', end="")
val = 'R$ ' + f'{sum(TotalFaturamento):.2f}'
print(f'{val:>27}')

str = 'Maior faturamento: '
print(f'{str:25}', end="")
print(f'{Produtos[TotalFaturamento.index(max(TotalFaturamento))]:>27}')

"""
Gerar 'Relatório II - Clientes - LOJA LAURA SMART” no formato de tabela
apresentando as seguintes informações sobre os clientes:
(a) Gastos de cada um dos clientes;
(b) Indicação do cliente responsável pelo maior gasto;
(c) Cálculo do valor médio gasto pelos clientes; e
(d) Indicação do cliente responsável pelo menor gasto.
"""

print('\nRelatório II - Clientes - LOJA LAURA SMART')
str = 'Clientes: '
print(f'{str:25}', end="")
for cliente in Clientes:
    print(f'{cliente:>27}',end="")
print()

str = 'Gastos: '
print(f'{str:25}', end="")
for(i, cliente) in enumerate(Clientes):
    val = 'R$ ' + f'{Gastos[i]:.2f}'
    print(f'{val:>27}', end="")
print()

str = 'Maior gasto: '
print(f'{str:25}', end="")
print(f'{Clientes[Gastos.index(max(Gastos))]:>27}')

str = 'Média de gastos: '
print(f'{str:25}', end="")
val = 'R$ ' + f'{sum(Gastos)/len(Gastos):.2f}'
print(f'{val:>27}')

str = 'Menor gasto: '
print(f'{str:25}', end="")
print(f'{Clientes[Gastos.index(min(Gastos))]:>27}')
