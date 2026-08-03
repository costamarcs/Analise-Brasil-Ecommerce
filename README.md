# Análise de Avaliações Negativas com NLP (spaCy) no E-commerce Brasileiro

[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/code)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
 
> **👉 [Clique aqui para acessar o Notebook no Kaggle](https://www.kaggle.com/code/marcoantoniocosta/analysis-with-nlp-spacy-low-customer-reviews)**

---

## 📋 Visão Geral do Projeto

Este projeto realiza uma investigação profunda sobre a **causa raiz da detração (avaliações negativas de 1 a 3 estrelas)** no e-commerce brasileiro, utilizando o renomado **Olist Brazilian E-commerce Dataset** disponível no Kaggle. 

Cruzando dados operacionais de logística e prazos com **Processamento de Linguagem Natural (NLP) via spaCy**, o estudo transforma milhares de comentários textuais brutos em indicadores estruturados e acionáveis, diagnosticando se a insatisfação do consumidor está atrelada a falhas dos lojistas ou a gargalos na malha logística.

---

## 🗃️ Sobre o Conjunto de Dados

O projeto utiliza o [**Brazilian E-Commerce Public Dataset by Olist**](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), que fornece uma visão rica e detalhada do comércio eletrônico no Brasil. 

* **Escala:** Abrange cerca de 100.000 pedidos realizados entre 2016 e 2018 em múltiplos marketplaces no Brasil.
* **Estrutura Relacional:** Os dados estão distribuídos em múltiplas tabelas interconectadas por chaves unificadas, cobrindo:
  * **Pedidos (`orders`):** Status, carimbos de data/hora de compra, aprovação, envio e entrega real vs. estimada.
  * **Avaliações (`order_reviews`):** Notas de 1 a 5 estrelas atribuídas pelos clientes, além de títulos e comentários textuais (cruciais para a análise de NLP).
  * **Itens e Produtos (`order_items`, `products`):** Detalhes dos produtos comercializados, categorias e informações de frete.
  * **Clientes (`customers`) e Vendedores (`sellers`):** Localização geográfica (CEP/Estado) e dados de lojistas parceiros.

---

## 📊 Principais Resultados & Insights de Negócio

1. **O Peso da Logística na Insatisfação:**  
   O atraso na entrega foi estatisticamente identificado como um dos principais vetores de avaliações de **1 estrela**. A insatisfação escala severamente quando o prazo estimado é ultrapassado em mais de 1 dia.
2. **Comportamento do Consumidor (Comentários vs. Notas):**  
   Cerca de **58,9%** das avaliações não possuem comentários textuais, mas a análise demonstra que clientes tendem a preencher feedback por texto predominantemente quando enfrentam experiências negativas severas. As avaliações de 1 estrela isoladamente superam a soma das avaliações de 2 e 3 estrelas.
3. **Superação de Limitações do Dataset via NLP:**  
   Como o dataset original carecía de flags diretas para o motivo do descumprimento de expectativas, a aplicação de **NLP com spaCy** permitiu extrair entidades, lemas e padrões semânticos dos comentários, estruturando drivers qualitativos de insatisfação em métricas quantificáveis.

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

### 1. No Kaggle (Opção Recomendada)
Você pode executar e interagir com o código diretamente no navegador através da plataforma do Kaggle, que já conta com o ambiente configurado e os datasets da Olist integrados:
* **[Acesse o Notebook no Kaggle](https://www.kaggle.com/code/marcoantoniocosta/analysis-with-nlp-spacy-low-customer-reviews)**
* *Dica:* Se preferir gerenciar via linha de comando no ambiente Kaggle ou automações, você pode utilizar a **Kaggle CLI** para baixar os datasets ou sincronizar o projeto.

### 2. Clonando o Repositório Localmente
Caso deseje clonar a estrutura base do projeto para o seu ambiente local:
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
