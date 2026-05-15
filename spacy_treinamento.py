import pandas as pd
import spacy
from spacy.tokens import DocBin

# 1. Carregar os dados que salvamos
df = pd.read_csv("dados_treino.csv", sep= ',', encoding= 'utf-8')

# 2. Criar um pipeline em português vazio apenas para estruturar o texto
nlp = spacy.blank("pt")

# 3. Inicializar o "balde" onde guardaremos nossos documentos processados
db = DocBin()

# 4. Loop pelas linhas do seu DataFrame do Pandas
for index, row in df.iterrows():
    # Cria o objeto Doc do spaCy baseado no texto do cliente
    doc = nlp.make_doc(str(row['review_text']))
    
    # Mapeia as colunas do Pandas para o dicionário que o spaCy espera
    doc.cats = {
        "PRODUTO": float(row['PRODUTO']),
        "LOGISTICA": float(row['LOGISTICA']),
        "PAGAMENTO": float(row['PAGAMENTO']),
        "PRECO": float(row['PRECO'])
    }
    
    # Adiciona o documento configurado ao balde
    db.add(doc)

# 5. Salva o balde de dados no disco rígido
db.to_disk(r"C:\Users\Marco\Desktop\Projetos\train.spacy")
print("Arquivo train.spacy gerado com sucesso!")
