import sqlite3
import pandas as pd
import pygsheets

# Autenticação via navegador (apenas na primeira vez)
gc = pygsheets.authorize(local=True)

# Criar ou abrir a planilha no Google Sheets
spreadsheet = gc.open("vendas")

# Selecionar a primeira aba da planilha
worksheet = spreadsheet[0]

# Conectar ao banco SQLite e buscar os dados
conn = sqlite3.connect("ecommerce.db")
df = pd.read_sql_query("SELECT * FROM vendas;", conn)
conn.close()

# Atualizar a planilha com os dados do DataFrame
worksheet.set_dataframe(df, (1, 1))

print("Dados exportados para o Google Sheets com sucesso! ✅")
