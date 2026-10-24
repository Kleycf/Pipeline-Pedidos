from transformar import pedido_para_linhas_fato


def test_pedido_com_dois_itens():
    pedido = {
        "id_pedido": 301,
        "data": "2026-10-20",
        "itens": [
            {
                "produto": {"Chave_Produto": 1, "Nome_Produto": "A", "Cor": "Azul"},
                "vendedor": {"Chave_Vendedor": 10, "Nome_Vendedor": "X"},
                "qtd": 2,
                "preco": 10.0,
            },
            {
                "produto": {"Chave_Produto": 2, "Nome_Produto": "B", "Cor": "Verde"},
                "vendedor": {"Chave_Vendedor": 20, "Nome_Vendedor": "Y"},
                "qtd": 3,
                "preco": 5.0,
            },
        ],
    }

    linhas = pedido_para_linhas_fato(pedido)

    assert len(linhas) == 2
    assert linhas[0]["valor_venda"] == 20.0
    assert linhas[1]["chave_vendedor"] == 20
