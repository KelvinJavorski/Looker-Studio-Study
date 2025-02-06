import sqlite3
import csv

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Consultar todas as vendas com detalhes de cliente, produto e data da venda
cursor.execute("""
SELECT v.id, c.nome AS cliente, p.nome AS produto, v.quantidade, v.total, v.data_venda
FROM vendas v
JOIN clientes c ON v.cliente_id = c.id
JOIN produtos p ON v.produto_id = p.id;
""")

# Exibir os resultados
resultados = cursor.fetchall()

# Criar e escrever no arquivo CSV
with open('vendas.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Adicionar a coluna "Data da Compra" no cabeçalho
    writer.writerow(['ID', 'Cliente', 'Produto', 'Quantidade', 'Total', 'Data da Compra'])
    
    # Escrever os dados no CSV, incluindo a data da compra
    writer.writerows(resultados)

conn.close()

print("Dados exportados para vendas.csv com sucesso!")
