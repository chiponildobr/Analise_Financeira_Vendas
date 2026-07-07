from src.relatorio import gerar_relatorio_excel
from src.ler_dados import carregar_dados
from src.limpeza import auditar_dados
from src.analises import (
    calcular_kpis,
    ranking_produtos,
    ranking_vendedores,
    vendas_por_forma_pagamento,
    ranking_estados,
    ranking_clientes,
)


def main():

    produtos, vendedores, clientes, vendas, estoque = carregar_dados()

    print("=" * 60)
    print(" SISTEMA DE ANÁLISE FINANCEIRA DE VENDAS ".center(60))
    print("=" * 60)

    print("\nBase de dados carregada com sucesso!\n")

    print(f"Produtos   : {len(produtos)}")
    print(f"Vendedores : {len(vendedores)}")
    print(f"Clientes   : {len(clientes)}")
    print(f"Vendas     : {len(vendas)}")
    print(f"Estoque    : {len(estoque)}")

    auditar_dados(produtos, vendedores, clientes, vendas, estoque)

    calcular_kpis(produtos, vendedores, clientes, vendas)

    ranking_produtos(produtos, vendas)
    ranking_vendedores(vendedores, vendas)
    vendas_por_forma_pagamento(vendas)
    ranking_estados(clientes, vendas)
    ranking_clientes(clientes, vendas)
    gerar_relatorio_excel(
    produtos,
    vendedores,
    clientes,
    vendas,
    estoque
)


if __name__ == "__main__":
    main()