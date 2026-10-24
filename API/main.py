from fastapi import FastAPI

app = FastAPI()

PEDIDOS = [
    {
        "id_pedido": 102,
        "data": "2026-10-16",
        "itens": [
            {
                "produto": {
                    "Chave_Produto": 5,
                    "Nome_Produto": "Produto A",
                    "Cor": "Azul",
                },
                "vendedor": {"Chave_Vendedor": 9, "Nome_Vendedor": "Vendedor X"},
                "qtd": 8,
                "preco": 25.50,
            }
        ],
    },
    {
        "id_pedido": 103,
        "data": "2026-10-16",
        "itens": [
            {
                "produto": {
                    "Chave_Produto": 2,
                    "Nome_Produto": "Produto B",
                    "Cor": "Vermelho",
                },
                "vendedor": {"Chave_Vendedor": 3, "Nome_Vendedor": "Vendedor Y"},
                "qtd": 3,
                "preco": 45.00,
            }
        ],
    },
    {
        "id_pedido": 104,
        "data": "2026-10-16",
        "itens": [
            {
                "produto": {
                    "Chave_Produto": 5,
                    "Nome_Produto": "Produto A",
                    "Cor": "Azul",
                },
                "vendedor": {"Chave_Vendedor": 7, "Nome_Vendedor": "Vendedor Z"},
                "qtd": 7,
                "preco": 100.00,
            }
        ],
    },
]


@app.get("/pedidos")
def listar_pedidos(pagina: int = 1, tamanho: int = 2):
    inicio = (pagina - 1) * tamanho
    fim = inicio + tamanho
    return PEDIDOS[inicio:fim]
