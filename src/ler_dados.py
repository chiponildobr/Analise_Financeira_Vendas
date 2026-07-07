import pandas as pd


def carregar_dados():
    produtos = pd.read_excel("dados/produtos.xlsx")
    vendedores = pd.read_excel("dados/vendedores.xlsx")
    clientes = pd.read_excel("dados/clientes.xlsx")
    vendas = pd.read_excel("dados/vendas.xlsx")
    estoque = pd.read_excel("dados/estoque.xlsx")

    return produtos, vendedores, clientes, vendas, estoque