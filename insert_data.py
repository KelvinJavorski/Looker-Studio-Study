import sqlite3
import random

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

clientes = [
    ("João Silva", "joao@email.com"),
    ("Maria Souza", "maria@email.com"),
    ("Carlos Lima", "carlos@email.com")
]

cursor.executemany(" INSERT INTO clientes (nome, email) VALUES(?, ?);", clientes)

produtos = [
    ("Notebook", 3500.00, "Eletrônicos"),
    ("Smartphone", 2200.00, "Eletrônicos"),
    ("Cadeira Gamer", 1200.00, "Móveis"),
    ("Monitor 27'", 1500.00, "Eletrônicos")
]

vendas = [
    (1, 1, 1, 3500.00),  # Cliente 1 compra 1 Notebook
    (2, 2, 2, 4400.00),  # Cliente 2 compra 2 Smartphones
    (3, 3, 1, 1200.00),  # Cliente 3 compra 1 Cadeira Gamer
]

cursor.executemany("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?);", produtos)

cursor.executemany("INSERT INTO vendas (cliente_id, produto_id, quantidade, total) VALUES (?, ?, ?, ?);", vendas)

conn.commit()
conn.close()

print("Dados inseridos")