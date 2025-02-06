import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Inserir clientes (novos nomes e emails)
clientes = [
    ("Ana Costa", "ana@email.com"),
    ("Beatriz Lima", "beatriz@email.com"),
    ("Daniel Rocha", "daniel@email.com"),
    ("Igor Silva", "igor@email.com"),
    ("Fernanda Souza", "fernanda@email.com"),
    ("Marcos Oliveira", "marcos@email.com"),
    ("Lucas Pereira", "lucas@email.com"),
    ("Juliana Santos", "juliana@email.com"),
    ("Renato Costa", "renato@email.com"),
    ("Carol Martins", "carol@email.com")
]

cursor.executemany("INSERT OR IGNORE INTO clientes (nome, email) VALUES(?, ?);", clientes)

# Inserir produtos (novos produtos)
produtos = [
    ("Notebook", 3500.00, "Eletrônicos"),
    ("Smartphone", 2200.00, "Eletrônicos"),
    ("Cadeira Gamer", 1200.00, "Móveis"),
    ("Monitor 27'", 1500.00, "Eletrônicos")
]

cursor.executemany("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?);", produtos)

# Função para gerar datas aleatórias entre 2025-01-01 e hoje
def gerar_data_aleatoria():
    dias_aleatorios = random.randint(0, 60)  # Até 60 dias atrás de 2025-01-01
    data_aleatoria = datetime.now() - timedelta(days=dias_aleatorios)
    return data_aleatoria.strftime('%Y-%m-%d')

# Inserir vendas com datas fictícias
vendas = [
    (1, 1, 1, 3500.00, gerar_data_aleatoria()),  # Cliente 1 compra 1 Notebook
    (2, 2, 2, 4400.00, gerar_data_aleatoria()),  # Cliente 2 compra 2 Smartphones
    (3, 3, 1, 1200.00, gerar_data_aleatoria()),  # Cliente 3 compra 1 Cadeira Gamer
    (1, 4, 1, 1500.00, gerar_data_aleatoria()),  # Cliente 1 compra 1 Monitor 27'
    (2, 1, 2, 7000.00, gerar_data_aleatoria()),  # Cliente 2 compra 2 Notebooks
    (3, 2, 1, 2200.00, gerar_data_aleatoria())   # Cliente 3 compra 1 Smartphone
]

cursor.executemany("INSERT INTO vendas (cliente_id, produto_id, quantidade, total, data_venda) VALUES (?, ?, ?, ?, ?);", vendas)

conn.commit()
conn.close()

print("Dados inseridos com datas fictícias")
