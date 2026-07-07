import os
import pandas as pd


def gerar_relatorio_excel(produtos, vendedores, clientes, vendas, estoque):

    os.makedirs("relatorios", exist_ok=True)

    vendas_relatorio = (
        vendas.merge(produtos, on="id_produto", how="left")
              .merge(vendedores, on="id_vendedor", how="left")
              .merge(clientes, on="id_cliente", how="left")
    )

    resumo = pd.DataFrame({
        "Indicador": [
            "Total de Produtos",
            "Total de Vendedores",
            "Total de Clientes",
            "Total de Vendas",
            "Faturamento Bruto",
            "Faturamento Líquido",
            "Total de Frete",
            "Total de Descontos"
        ],
        "Valor": [
            len(produtos),
            len(vendedores),
            len(clientes),
            len(vendas),
            vendas["valor_bruto"].sum(),
            vendas["valor_total"].sum(),
            vendas["frete"].sum(),
            vendas["desconto"].sum()
        ]
    })

    caminho = "relatorios/Relatorio_Financeiro.xlsx"

    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:

        resumo.to_excel(writer,
                         sheet_name="Resumo",
                         index=False)

        produtos.to_excel(writer,
                          sheet_name="Produtos",
                          index=False)

        vendedores.to_excel(writer,
                            sheet_name="Vendedores",
                            index=False)

        clientes.to_excel(writer,
                          sheet_name="Clientes",
                          index=False)

        vendas.to_excel(writer,
                        sheet_name="Vendas",
                        index=False)

        estoque.to_excel(writer,
                         sheet_name="Estoque",
                         index=False)

        vendas_relatorio.to_excel(writer,
                                  sheet_name="Base Completa",
                                  index=False)

    print("\n")
    print("Arquivo salvo em:")
    print(caminho)