import sqlite3
import csv

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Consultar todas as vendas com detalhes de cliente e produto
cursor.execute("""
SELECT v.id, c.nome AS cliente, p.nome AS produto, v.quantidade, v.total
FROM vendas v
JOIN clientes c ON v.cliente_id = c.id
JOIN produtos p ON v.produto_id = p.id;
""")

# Exibir os resultados
resultados = cursor.fetchall()

with open('vendas.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Cliente', 'Produto', 'Quantidade', 'Total'])
    writer.writerows(resultados)

conn.close()