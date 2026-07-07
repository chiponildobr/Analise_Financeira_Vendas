def calcular_kpis(produtos, vendedores, clientes, vendas):
    print("\n" + "=" * 60)
    print(" INDICADORES DE DESEMPENHO ".center(60))
    print("=" * 60)

    vendas_validas = vendas[vendas["status"] == "Concluída"]

    faturamento_bruto = vendas_validas["valor_bruto"].sum()
    faturamento_liquido = vendas_validas["valor_total"].sum()
    total_descontos = vendas_validas["desconto"].sum()
    total_frete = vendas_validas["frete"].sum()
    ticket_medio = vendas_validas["valor_total"].mean()
    quantidade_vendas = len(vendas_validas)
    quantidade_itens = vendas_validas["quantidade"].sum()

    print(f"Faturamento Bruto     : R$ {faturamento_bruto:,.2f}")
    print(f"Faturamento Líquido   : R$ {faturamento_liquido:,.2f}")
    print(f"Total de Descontos    : R$ {total_descontos:,.2f}")
    print(f"Total de Fretes       : R$ {total_frete:,.2f}")
    print(f"Ticket Médio          : R$ {ticket_medio:,.2f}")
    print(f"Vendas Concluídas     : {quantidade_vendas}")
    print(f"Itens Vendidos        : {quantidade_itens}")


def ranking_produtos(produtos, vendas):
    print("\n" + "=" * 60)
    print(" TOP 10 PRODUTOS POR FATURAMENTO ".center(60))
    print("=" * 60)

    vendas_validas = vendas[vendas["status"] == "Concluída"]

    base = vendas_validas.merge(
        produtos,
        on="id_produto",
        how="left"
    )

    ranking = (
        base.groupby("produto")["valor_total"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(ranking)


def ranking_vendedores(vendedores, vendas):
    print("\n" + "=" * 60)
    print(" RANKING DE VENDEDORES ".center(60))
    print("=" * 60)

    vendas_validas = vendas[vendas["status"] == "Concluída"]

    base = vendas_validas.merge(
        vendedores,
        on="id_vendedor",
        how="left"
    )

    ranking = (
        base.groupby("nome")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    print(ranking)


def vendas_por_forma_pagamento(vendas):
    print("\n" + "=" * 60)
    print(" VENDAS POR FORMA DE PAGAMENTO ".center(60))
    print("=" * 60)

    vendas_validas = vendas[vendas["status"] == "Concluída"]

    resultado = (
        vendas_validas.groupby("forma_pagamento")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    print(resultado)


def ranking_estados(clientes, vendas):
    print("\n" + "=" * 60)
    print(" FATURAMENTO POR ESTADO ".center(60))
    print("=" * 60)

    vendas_validas = vendas[vendas["status"] == "Concluída"]

    base = vendas_validas.merge(
        clientes[["id_cliente", "estado"]],
        on="id_cliente",
        how="left"
    )

    ranking = (
        base.groupby("estado")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    print(ranking)


def ranking_clientes(clientes, vendas):
    print("\n" + "=" * 60)
    print(" TOP 10 CLIENTES ".center(60))
    print("=" * 60)

    vendas_validas = vendas[vendas["status"] == "Concluída"]

    base = vendas_validas.merge(
        clientes[["id_cliente", "cliente"]],
        on="id_cliente",
        how="left"
    )

    ranking = (
        base.groupby("cliente")["valor_total"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(ranking)