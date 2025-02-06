import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Conectar ao banco de dados e realizar uma consulta
conn = sqlite3.connect("ecommerce.db")
df = pd.read_sql_query("""
SELECT v.id, c.nome AS cliente, p.nome AS produto, v.quantidade, v.total, v.data_venda
FROM vendas v
JOIN clientes c ON v.cliente_id = c.id
JOIN produtos p ON v.produto_id = p.id;
""", conn)
conn.close()

# Estatísticas básicas
print(df.describe())

# Gráfico de vendas totais por produto
df.groupby('produto')['total'].sum().plot(kind='bar')
plt.title('Vendas totais por produto')
plt.ylabel('Total de Vendas')
plt.show()

# Vendas ao longo do tempo
df['data_venda'] = pd.to_datetime(df['data_venda'])
df.groupby(df['data_venda'].dt.to_period('M'))['total'].sum().plot(kind='line')
plt.title('Vendas ao longo do tempo')
plt.ylabel('Total de Vendas')
plt.show()
