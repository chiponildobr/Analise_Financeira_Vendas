import os
import random
from datetime import datetime, timedelta

import pandas as pd

from produtos import produtos
from vendedores import vendedores
from localidades import localidades
from parametros import formas_pagamento, status_venda, canais_venda


def escolher_item(lista):
    return random.choice(lista)


def gerar_clientes(qtd_clientes=500):
    nomes = [
        "João Almeida", "Maria Santos", "Pedro Lima", "Ana Costa",
        "Lucas Martins", "Fernanda Rocha", "Rafael Souza", "Camila Ferreira",
        "Bruno Oliveira", "Juliana Ribeiro", "Marcos Silva", "Patrícia Gomes"
    ]

    clientes = []

    for id_cliente in range(1, qtd_clientes + 1):
        local = escolher_item(localidades)

        clientes.append({
            "id_cliente": id_cliente,
            "cliente": escolher_item(nomes),
            "estado": local["estado"],
            "cidade": local["cidade"],
            "regiao": local["regiao"]
        })

    return pd.DataFrame(clientes)


def gerar_vendas(df_produtos, df_clientes, df_vendedores, qtd_vendas=5000):
    vendas = []
    data_inicio = datetime(2025, 1, 1)

    for id_venda in range(100001, 100001 + qtd_vendas):
        produto = df_produtos.sample(1).iloc[0]
        cliente = df_clientes.sample(1).iloc[0]
        vendedor = df_vendedores.sample(1).iloc[0]

        quantidade = random.randint(1, 6)
        desconto = escolher_item([0, 10, 25, 50, 75, 100])
        frete = escolher_item([0, 20, 35, 50, 75])

        valor_bruto = quantidade * produto["preco"]
        valor_total = valor_bruto - desconto + frete

        vendas.append({
            "id_venda": id_venda,
            "data_venda": data_inicio + timedelta(days=random.randint(0, 729)),
            "id_produto": produto["id_produto"],
            "id_cliente": cliente["id_cliente"],
            "id_vendedor": vendedor["id_vendedor"],
            "quantidade": quantidade,
            "valor_bruto": valor_bruto,
            "desconto": desconto,
            "frete": frete,
            "valor_total": valor_total,
            "forma_pagamento": escolher_item(formas_pagamento),
            "status": escolher_item(status_venda),
            "canal_venda": escolher_item(canais_venda)
        })

    return pd.DataFrame(vendas)


def gerar_estoque(df_produtos):
    estoque = []

    for _, produto in df_produtos.iterrows():
        estoque.append({
            "id_produto": produto["id_produto"],
            "produto": produto["produto"],
            "estoque_atual": random.randint(20, 500),
            "estoque_minimo": random.randint(10, 80)
        })

    return pd.DataFrame(estoque)


def inserir_erros_teste(df_vendas):
    df_vendas.loc[10, "id_produto"] = None
    df_vendas.loc[25, "quantidade"] = -3
    df_vendas.loc[40, "frete"] = -20
    df_vendas.loc[55, "valor_total"] = 0
    df_vendas.loc[80, "id_venda"] = df_vendas.loc[79, "id_venda"]

    return df_vendas


def main():
    os.makedirs("dados", exist_ok=True)

    df_produtos = pd.DataFrame(produtos)
    df_produtos.insert(0, "id_produto", range(1, len(df_produtos) + 1))

    df_vendedores = pd.DataFrame(vendedores)
    df_clientes = gerar_clientes()
    df_vendas = gerar_vendas(df_produtos, df_clientes, df_vendedores)
    df_vendas = inserir_erros_teste(df_vendas)
    df_estoque = gerar_estoque(df_produtos)

    df_produtos.to_excel("dados/produtos.xlsx", index=False)
    df_vendedores.to_excel("dados/vendedores.xlsx", index=False)
    df_clientes.to_excel("dados/clientes.xlsx", index=False)
    df_vendas.to_excel("dados/vendas.xlsx", index=False)
    df_estoque.to_excel("dados/estoque.xlsx", index=False)

    print("Bases criadas na pasta dados.")


if __name__ == "__main__":
    main()