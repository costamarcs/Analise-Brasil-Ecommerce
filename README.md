# Análise de Avaliações Negativas com NLP (spaCy) no E-commerce Brasileiro

[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/code)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)

---

## 📋 Visão Geral do Projeto

Este projeto realiza uma investigação profunda sobre a **causa raiz da detração (avaliações negativas de 1 a 3 estrelas)** no e-commerce brasileiro, utilizando o renomado **Olist Brazilian E-commerce Dataset** disponível no Kaggle. 

Cruzando dados operacionais de logística e prazos com **Processamento de Linguagem Natural (NLP) via spaCy**, o estudo transforma milhares de comentários textuais brutos em indicadores estruturados e acionáveis, diagnosticando se a insatisfação do consumidor está atrelada a falhas dos lojistas ou a gargalos na malha logística.

---

## 📊 Principais Resultados & Insights de Negócio

1. **O Peso da Logística na Insatisfação:**  
   O atraso na entrega foi estatisticamente identificado como um dos principais vetores de avaliações de **1 estrela** (que isoladamente superam a soma das avaliações de 2 e 3 estrelas). A insatisfação escala severamente quando o prazo estimado é ultrapassado em mais de 1 dia.
2. **Comportamento do Consumidor (Comentários vs. Notas):**  
   Cerca de **58,9%** das avaliações não possuem comentários textuais, mas a análise demonstra que clientes tendem a preencher feedback por texto predominantemente quando enfrentam experiências negativas severas.
3. **Superação de Limitações do Dataset via NLP:**  
   Como o dataset original carecia de flags diretas para o motivo do descumprimento de expectativas, a aplicação de **NLP com spaCy** permitiu extrair entidades, lemas e padrões semânticos dos comentários, estruturando drivers qualitativos de insatisfação em métricas quantificáveis.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.12
* **Manipulação e Análise de Dados:** Pandas, NumPy
* **Processamento de Linguagem Natural:** spaCy (Tokenização, Lematização, Extração de Padrões)
* **Visualização de Dados:** Matplotlib, Seaborn (com paletas de cores customizadas)
* **Ambiente de Desenvolvimento:** Kaggle Notebooks

---

## 🗂️ Estrutura das Análises no Notebook

1. **Introdução e Contextualização:** Alinhamento do problema de negócio e escopo da análise de detração.
2. **Preparação do Ambiente:** Importação de pacotes, padronização de temas visuais e merge de múltiplos datasets relacionais da Olist (`orders`, `reviews`, `customers`, `order_items`).
3. **Engenharia de Atributos e Classificadores Operacionais:** Criação de colunas customizadas (`delivery_status`, `seller_sla_status`, `delivery_time_status`) para cruzar prazos estimados vs. reais.
4. **Análise Exploratória de Dados (EDA):** Distribuição de notas, proporção de comentários preenchidos vs. vazios e comportamento temporal.
5. **Processamento de Linguagem Natural (NLP):** Extração de insights textuais e união com os KPIs operacionais para fechar o diagnóstico logístico.

---

## 🚀 Como Executar o Projeto

Você pode interagir com este projeto de duas maneiras:

### Opção 1 — Kaggle (Recomendado)
Acesse e execute o código interativamente no navegador sem precisar instalar nada:
* **[Link Direto para o Notebook no Kaggle](https://www.kaggle.com/code/marcoantoniocosta/analysis-with-nlp-spacy-low-customer-reviews)**

### Opção 2 — Execução Local
Caso deseje rodar o ambiente na sua máquina:
```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

# Entre no diretório
cd seu-repositorio

# Instale as dependências necessárias
pip install pandas numpy matplotlib seaborn spacy

# Baixe os datasets da Olist no Kaggle e execute o notebook Jupyter
jupyter notebook
