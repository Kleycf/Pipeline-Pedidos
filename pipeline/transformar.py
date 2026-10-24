def pedido_para_linhas_fato(pedido):
    linhas = []
    for itens in pedido["itens"]:
        linhas.append(
            {
                "id_pedido": pedido["id_pedido"],
                "chave_produto": itens["produto"]["Chave_Produto"],
                "chave_vendedor": itens["vendedor"]["Chave_Vendedor"],
                "quantidade": itens["qtd"],
                "valor_venda": itens["qtd"] * itens["preco"],
                "data": pedido["data"],
                "nome_vendedor": itens["vendedor"]["Nome_Vendedor"],
                "cor": itens["produto"]["Cor"],
                "nome_produto": itens["produto"]["Nome_Produto"],
            }
        )

    return linhas
