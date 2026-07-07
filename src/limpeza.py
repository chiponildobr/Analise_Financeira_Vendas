def auditar_dados(produtos, vendedores, clientes, vendas, estoque):
    print("\n" + "=" * 60)
    print(" RELATÓRIO DE QUALIDADE DOS DADOS ".center(60))
    print("=" * 60)

    total_registros = len(vendas)

    ids_duplicados = vendas["id_venda"].duplicated().sum()
    valores_nulos = vendas.isnull().sum().sum()
    qtd_negativa = (vendas["quantidade"] < 0).sum()
    frete_negativo = (vendas["frete"] < 0).sum()
    valor_zerado = (vendas["valor_total"] <= 0).sum()

    produtos_invalidos = ~vendas["id_produto"].isin(produtos["id_produto"])
    clientes_invalidos = ~vendas["id_cliente"].isin(clientes["id_cliente"])
    vendedores_invalidos = ~vendas["id_vendedor"].isin(vendedores["id_vendedor"])

    total_erros = (
        ids_duplicados
        + valores_nulos
        + qtd_negativa
        + frete_negativo
        + valor_zerado
        + produtos_invalidos.sum()
        + clientes_invalidos.sum()
        + vendedores_invalidos.sum()
    )

    qualidade = 100 - ((total_erros / total_registros) * 100)

    print(f"Registros analisados      : {total_registros}")
    print(f"IDs duplicados            : {ids_duplicados}")
    print(f"Valores nulos             : {valores_nulos}")
    print(f"Quantidade negativa       : {qtd_negativa}")
    print(f"Frete negativo            : {frete_negativo}")
    print(f"Valor total zerado        : {valor_zerado}")
    print(f"Produtos inexistentes     : {produtos_invalidos.sum()}")
    print(f"Clientes inexistentes     : {clientes_invalidos.sum()}")
    print(f"Vendedores inexistentes   : {vendedores_invalidos.sum()}")
    print(f"\nQualidade da base         : {qualidade:.2f}%")