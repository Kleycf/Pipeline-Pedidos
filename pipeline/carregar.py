import os
import sqlite3

DB_PATH = os.environ.get("DB_PATH", "fato.db")


def carregar_linhas(linhas):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS FATO_Vendas (
            id_pedido INTEGER PRIMARY KEY,
            chave_produto INTEGER,
            chave_vendedor INTEGER,
            quantidade INTEGER,
            valor_venda REAL,
            data TEXT) """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS DIM_Vendedor(
            chave_vendedor INTEGER PRIMARY KEY,
            nome_vendedor TEXT)
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS DIM_Produto(
            chave_produto INTEGER PRIMARY KEY,
            nome_produto TEXT,
            cor TEXT)
        """
    )

    cursor.execute("DELETE FROM FATO_Vendas")
    cursor.execute("DELETE FROM DIM_Vendedor")
    cursor.execute("DELETE FROM DIM_Produto")

    for linha in linhas:
        cursor.execute(
            "INSERT OR REPLACE INTO FATO_Vendas (id_pedido, chave_produto, chave_vendedor, quantidade, valor_venda, data) VALUES (?,?,?,?,?,?)",
            (
                linha["id_pedido"],
                linha["chave_produto"],
                linha["chave_vendedor"],
                linha["quantidade"],
                linha["valor_venda"],
                linha["data"],
            ),
        )
    for linha in linhas:
        cursor.execute(
            "INSERT OR REPLACE INTO DIM_Vendedor (chave_vendedor,nome_vendedor)VALUES(?,?)",
            (
                linha["chave_vendedor"],
                linha["nome_vendedor"],
            ),
        )
    for linha in linhas:
        cursor.execute(
            "INSERT OR REPLACE INTO DIM_Produto (chave_produto,nome_produto,cor)VALUES(?,?,?)",
            (
                linha["chave_produto"],
                linha["nome_produto"],
                linha["cor"],
            ),
        )

    conn.commit()
    conn.close()
