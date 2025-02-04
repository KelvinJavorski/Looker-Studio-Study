📊 Projeto de Análise de Dados com Python, SQL e Looker Studio

## 📌 Sobre o Projeto
Este projeto tem como objetivo explorar dados de um e-commerce, armazená-los em um banco de dados SQLite e gerar relatórios e gráficos interativos no Looker Studio.

## 🛠️ Tecnologias Utilizadas
- **Python**: Para manipulação e análise de dados.
- **SQLite**: Banco de dados leve para armazenamento das informações.
- **Looker Studio**: Para visualização e análise de dados.
- **Git/GitHub**: Controle de versão e colaboração.

## 📂 Estrutura do Projeto
```
📁 Dados-LockerStudio
│-- 📜 setup_database.py  # Criação do banco de dados e tabelas
│-- 📜 insert_data.py     # Inserção de dados fictícios no banco
│-- 📜 consultas.py       # Consultas SQL para análise de dados
│-- 📜 README.md          # Documentação do projeto
│-- 📜 requirements.txt   # Dependências do projeto
```

## 🔧 Configuração do Ambiente
1. **Clonar o repositório**
   ```bash
   git clone https://github.com/SEU-USUARIO/Looker-Studio-Study.git
   cd Looker-Studio-Study
   ```

2. **Criar um ambiente virtual e ativá-lo**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

## 🏗️ Como Executar o Projeto
1. **Criar o banco de dados e as tabelas**
   ```bash
   python setup_database.py
   ```
2. **Inserir dados no banco**
   ```bash
   python insert_data.py
   ```
3. **Executar consultas para análise**
   ```bash
   python consultas.py
   ```

## 📈 Integração com Looker Studio
Para visualizar os dados no **Looker Studio**:
1. Conecte o **Google Sheets** ao seu banco de dados SQLite exportando os dados.
2. Importe os dados do **Google Sheets** para o **Looker Studio**.
3. Crie gráficos e dashboards interativos.

## 📌 Consultas SQL de Exemplo
```sql
-- Total de vendas por cliente
SELECT clientes.nome, SUM(vendas.total) AS total_gasto
FROM vendas
JOIN clientes ON vendas.cliente_id = clientes.id
GROUP BY clientes.nome
ORDER BY total_gasto DESC;
```

## 🚀 Melhorias Futuras
- Automatizar a exportação dos dados para Google Sheets.
- Implementar gráficos dinâmicos diretamente no Python.
- Explorar outras fontes de dados e APIs.

## 🤝 Contribuição
Sinta-se à vontade para contribuir com o projeto! Para isso:
1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua feature.
3. Envie um **pull request**.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

---
📧 **Contato:** Caso tenha dúvidas, me envie uma mensagem!

