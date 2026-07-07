import os
import matplotlib.pyplot as plt


def gerar_grafico_top_produtos(produtos, vendas):
    os.makedirs("graficos", exist_ok=True)

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

    plt.figure(figsize=(10, 6))

    ranking.plot(kind="bar")

    plt.title("Top 10 Produtos por Faturamento")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("graficos/top_produtos.png")

    plt.close()

    print("Gráfico criado com sucesso.")