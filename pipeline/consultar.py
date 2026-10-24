import sqlite3

conn = sqlite3.connect("fato.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM FATO_Vendas")

for linha in cursor.fetchall():
    print(linha)

cursor.execute("SELECT * FROM DIM_Vendedor")

for linha in cursor.fetchall():
    print(linha)

cursor.execute("SELECT * FROM DIM_Produto")

for linha in cursor.fetchall():
    print(linha)

cursor.execute(
    """
                    SELECT dv.nome_vendedor,SUM(fv.valor_venda) FROM FATO_Vendas fv
                        INNER JOIN DIM_Vendedor dv 
                            on dv.chave_vendedor = fv.chave_vendedor
                        INNER JOIN DIM_Produto dp
                            on dp.chave_produto = fv.chave_produto
                        GROUP BY dv.nome_vendedor
"""
)

for linha in cursor.fetchall():
    print(linha)

conn.close()
