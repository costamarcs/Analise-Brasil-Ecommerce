import pandas as pd
from sqlalchemy import create_engine
import os

# 1. Configurações de conexão (Substitua pelos seus dados)
usuario = 'postgres'
senha = 'marco123'
host = 'localhost'
porta = '5432'
banco = 'Brasil_olist'

# Criar a engine de conexão
engine = create_engine(f'postgresql://{usuario}:{senha}@{host}:{porta}/{banco}')

# 2. Caminho dos arquivos
pasta_dados = r'C:\Users\Marco\Desktop\Projetos\Brasil_olist_ecommerce'
arquivos = [f for f in os.listdir(pasta_dados) if f.endswith('.csv')]

# 3. Loop de Carga
for arquivo in arquivos:
    nome_tabela = arquivo.replace('.csv', '')
    df = pd.read_csv(os.path.join(pasta_dados, arquivo))
    
    # Enviar para o Postgres
    # 'if_exists=replace' recria a tabela se ela já existir
    df.to_sql(nome_tabela, engine, if_exists='replace', index=False)
    print(f"Tabela {nome_tabela} carregada no PostgreSQL!")