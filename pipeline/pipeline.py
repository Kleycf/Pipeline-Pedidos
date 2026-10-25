import requests
import os

from transformar import pedido_para_linhas_fato
from carregar import carregar_linhas

URL_API = os.environ.get("URL_API", "http://127.0.0.1:8000")


def extrair_pedidos():

    pagina = 1

    total_pedidos = []

    while True:
        resposta = requests.get(
            f"{URL_API}/pedidos",
            params={"pagina": pagina},
        )

        if resposta.status_code != 200:
            raise Exception(
                f"Erro na requisição: {resposta.status_code} - Descrição de Erro: {resposta.text} - Pagina {pagina}"
            )

        pedidos = resposta.json()

        if len(pedidos) == 0:
            break

        total_pedidos.extend(pedidos)
        pagina += 1

    return total_pedidos


pedidos = extrair_pedidos()

todas_linhas = []


for pedido in pedidos:
    linhas = pedido_para_linhas_fato(pedido)
    todas_linhas.extend(linhas)


carregar_linhas(todas_linhas)
