# Pipeline de Big Data - Análise de Filmes
## Projeto Final - Fundamentos de Big Data

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ptojal1/projeto-bigdata-av2/blob/main/notebooks/movies_pipeline_completo_AV2.ipynb)
[![GitHub](https://img.shields.io/badge/GitHub-ptojal1%2Fprojeto--bigdata--av2-blue?logo=github)](https://github.com/ptojal1/projeto-bigdata-av2)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)

**Instituição:** Cesar School 
**Disciplina:** Fundamentos de Big Data  
**Equipe:**
- Pedro Tojal
- Henrique Leal
- Gabriel Galdino
- Lorenzo Marcelino

**Data:** Dezembro de 2025

**🔗 Links Rápidos:**
- [📓 Executar no Google Colab](https://colab.research.google.com/github/ptojal1/projeto-bigdata-av2/blob/main/notebooks/movies_pipeline_completo_AV2.ipynb)
- [📖 Guia do Colab](GUIA_COLAB.md)
- [✅ Checklist AV2](CHECKLIST_AV2.md)
- [🏗️ Arquitetura](documentacao/ARQUITETURA.md)

---

## 📋 Sumário

1. [Introdução](#introdução)
2. [Motivação](#motivação)
3. [Objetivo do Projeto](#objetivo-do-projeto)
4. [Metodologia (Pipeline de Dados)](#metodologia-pipeline-de-dados)
   - 4.1 [Fontes de Dados](#41-fontes-de-dados)
   - 4.2 [Ingestão](#42-ingestão)
   - 4.3 [Transformação](#43-transformação)
   - 4.4 [Carregamento](#44-carregamento)
   - 4.5 [Destino](#45-destino)
5. [Arquitetura Medallion](#arquitetura-medallion)
6. [Resultados e Visualizações](#resultados-e-visualizações)
7. [Conclusões](#conclusões)
8. [Trabalhos Futuros](#trabalhos-futuros)
9. [Referências](#referências)
10. [Como Executar](#como-executar)

---

## 1. Introdução

Este projeto apresenta a implementação de um **pipeline completo de Big Data** para análise da indústria cinematográfica, utilizando o dataset "The Movies Dataset" disponível no Kaggle. O pipeline foi desenvolvido seguindo a **arquitetura Medallion** (Bronze, Silver, Gold), que organiza o processamento de dados em camadas progressivas de refinamento e qualidade.

A indústria do cinema movimenta bilhões de dólares anualmente e gera uma quantidade massiva de dados relacionados a bilheterias, avaliações de usuários, metadados de filmes, elencos e equipes técnicas. Compreender os padrões presentes nesses dados pode fornecer insights valiosos para produtores, distribuidores, investidores e até mesmo para o público consumidor.

Este trabalho demonstra a aplicação prática dos conceitos de Big Data aprendidos em sala de aula, desde a ingestão de dados brutos até a geração de visualizações interativas e insights acionáveis.

---

## 2. Motivação

A escolha do tema "Análise da Indústria Cinematográfica" foi motivada por diversos fatores:

### 2.1 Relevância Econômica
A indústria cinematográfica global movimentou mais de **US$ 100 bilhões** em 2023, sendo um dos setores mais relevantes da economia criativa mundial.

### 2.2 Disponibilidade de Dados
O Kaggle disponibiliza datasets públicos e de alta qualidade sobre filmes, contendo milhares de registros com informações detalhadas sobre produções cinematográficas.

### 2.3 Aplicabilidade Prática
Os insights gerados podem auxiliar:
- **Produtores:** Decisões sobre investimento em projetos
- **Distribuidores:** Estratégias de lançamento e marketing
- **Investidores:** Análise de risco e retorno
- **Público:** Recomendações personalizadas de conteúdo

### 2.4 Complexidade Adequada
O dataset apresenta características ideais para um projeto de Big Data:
- Dados estruturados e semi-estruturados
- Volume considerável (milhares de filmes)
- Diversidade de atributos (numéricos, textuais, temporais)
- Necessidade de limpeza e transformação

---

## 3. Objetivo do Projeto

### 3.1 Objetivo Geral
Desenvolver um **pipeline completo de Big Data** para análise da indústria cinematográfica, gerando insights sobre tendências de mercado, fatores de sucesso e padrões de comportamento da audiência.

### 3.2 Objetivos Específicos
1. **Implementar um pipeline ETL robusto** seguindo a arquitetura Medallion
2. **Analisar tendências temporais** na indústria do cinema (décadas, anos, meses)
3. **Identificar fatores de sucesso** (gêneros lucrativos, diretores de destaque, etc.)
4. **Avaliar a relação entre orçamento e receita** (ROI - Return on Investment)
5. **Analisar o comportamento das avaliações** de usuários
6. **Criar visualizações interativas** e dashboards para comunicação dos insights
7. **Documentar todo o processo** seguindo boas práticas de engenharia de dados

---

## 4. Metodologia (Pipeline de Dados)

O pipeline foi desenvolvido seguindo as etapas clássicas de processamento de dados em Big Data:

### 4.1 Fontes de Dados

**Dataset Utilizado:** The Movies Dataset (Kaggle)

**Descrição:** Dataset público contendo informações sobre mais de 45.000 filmes, incluindo:
- `movies_metadata.csv`: Metadados de filmes (título, orçamento, receita, data de lançamento, etc.)
- `credits.csv`: Informações sobre elenco e equipe técnica
- `ratings.csv`: Avaliações de usuários

**Características:**
- **Volume:** ~45.000 filmes
- **Variedade:** Dados estruturados (CSV) com campos numéricos, textuais e JSON aninhados
- **Veracidade:** Dados do TMDB (The Movie Database), reconhecida fonte de informações cinematográficas

### 4.2 Ingestão

**Tipo:** Batch (lote)

**Ferramentas Utilizadas:**
- `pandas`: Leitura de arquivos CSV
- `requests`: Download de datasets do Kaggle
- Google Colab: Ambiente de execução

**Processo:**
1. Download manual do dataset do Kaggle
2. Upload para Google Drive (integração com Colab)
3. Leitura dos arquivos CSV usando `pandas.read_csv()`
4. Armazenamento inicial na camada **Bronze** (dados brutos)

**Código Exemplo:**
```python
import pandas as pd

# Ingestão de dados brutos
movies_df = pd.read_csv('/content/drive/MyDrive/movies_data/movies_metadata.csv', low_memory=False)
credits_df = pd.read_csv('/content/drive/MyDrive/movies_data/credits.csv')
ratings_df = pd.read_csv('/content/drive/MyDrive/movies_data/ratings.csv')
```

### 4.3 Transformação

**Camada:** Silver (dados limpos e transformados)

**Ferramentas Utilizadas:**
- `pandas`: Manipulação de dados
- `numpy`: Operações numéricas
- `json`: Parse de campos JSON aninhados

**Processos de Transformação:**

#### 4.3.1 Limpeza de Dados
- Remoção de duplicatas
- Tratamento de valores nulos
- Correção de tipos de dados
- Remoção de registros inválidos (ex: orçamento = 0)

#### 4.3.2 Normalização
- Conversão de datas para formato datetime
- Padronização de nomes de colunas
- Parse de campos JSON (gêneros, produtoras, etc.)

#### 4.3.3 Enriquecimento
- Criação de campos derivados:
  - `profit`: Receita - Orçamento
  - `roi`: (Receita / Orçamento - 1) * 100
  - `release_year`: Ano de lançamento
  - `release_decade`: Década de lançamento
  - `budget_category`: Classificação de orçamento (Low, Medium, High)

#### 4.3.4 Agregações
- Cálculos por gênero, ano, década
- Estatísticas descritivas
- Rankings e top N

**Código Exemplo:**
```python
# Limpeza e transformação
movies_clean = movies_df.copy()

# Converter tipos
movies_clean['release_date'] = pd.to_datetime(movies_clean['release_date'], errors='coerce')
movies_clean['budget'] = pd.to_numeric(movies_clean['budget'], errors='coerce')
movies_clean['revenue'] = pd.to_numeric(movies_clean['revenue'], errors='coerce')

# Remover filmes sem orçamento/receita
movies_clean = movies_clean[(movies_clean['budget'] > 0) & (movies_clean['revenue'] > 0)]

# Criar campos derivados
movies_clean['profit'] = movies_clean['revenue'] - movies_clean['budget']
movies_clean['roi'] = ((movies_clean['revenue'] / movies_clean['budget']) - 1) * 100
movies_clean['release_year'] = movies_clean['release_date'].dt.year
movies_clean['release_decade'] = (movies_clean['release_year'] // 10) * 10
```

### 4.4 Carregamento

**Camada:** Gold (dados refinados para análise)

**Ferramentas Utilizadas:**
- `pandas`: Exportação de dados
- `pyarrow`: Formato Parquet (mais eficiente)

**Processo:**
1. Criação de datasets agregados e otimizados
2. Salvamento em formatos eficientes (CSV, Parquet)
3. Armazenamento na camada **Gold**

**Código Exemplo:**
```python
# Salvamento na camada Gold
movies_clean.to_parquet('/content/dados/gold/movies_gold.parquet', index=False)
movies_clean.to_csv('/content/dados/gold/movies_gold.csv', index=False)
```

### 4.5 Destino

**Local Final:** Camada Gold + Visualizações no Notebook

**Ferramentas de Visualização:**
- `plotly`: Gráficos interativos
- `matplotlib`: Gráficos estáticos
- `seaborn`: Visualizações estatísticas

**Consumo dos Dados:**
- Análise exploratória no Jupyter/Colab
- Dashboards interativos
- Relatórios com insights

---

## 5. Arquitetura Medallion

O projeto segue a **arquitetura Medallion**, que organiza o processamento de dados em três camadas:

```
┌─────────────────────────────────────────────────────┐
│                   FONTES DE DADOS                   │
│              (Kaggle - The Movies Dataset)           │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│               CAMADA BRONZE (Raw Data)              │
│  - Dados brutos sem transformação                   │
│  - Formato original (CSV)                           │
│  - Armazenamento: /dados/bronze/                    │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│             CAMADA SILVER (Cleaned Data)            │
│  - Dados limpos e normalizados                      │
│  - Tipos de dados corrigidos                        │
│  - Valores nulos tratados                           │
│  - Armazenamento: /dados/silver/                    │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│            CAMADA GOLD (Business-Ready Data)        │
│  - Dados agregados e enriquecidos                   │
│  - Métricas de negócio calculadas                   │
│  - Otimizado para consultas                         │
│  - Armazenamento: /dados/gold/                      │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│            VISUALIZAÇÕES E DASHBOARDS               │
│  - Gráficos interativos (Plotly)                    │
│  - Insights e análises                              │
│  - Relatórios finais                                │
└─────────────────────────────────────────────────────┘
```

### Benefícios da Arquitetura Medallion:
1. **Rastreabilidade:** Sempre é possível voltar aos dados brutos
2. **Qualidade Progressiva:** Cada camada adiciona valor aos dados
3. **Reutilização:** Dados limpos podem ser usados em múltiplas análises
4. **Performance:** Dados Gold otimizados para consultas rápidas
5. **Manutenibilidade:** Facilita identificar onde erros ocorreram

---

## 6. Resultados e Visualizações

### 6.1 Análise Temporal

**Insight 1: Evolução do Orçamento Médio ao Longo das Décadas**
- Observou-se um crescimento exponencial nos orçamentos a partir dos anos 1990
- O orçamento médio na década de 2010 é **10x maior** que nos anos 1980

**Visualização:**
- Gráfico de linha mostrando orçamento médio por década

**Insight 2: Número de Filmes Produzidos por Ano**
- Pico de produção cinematográfica em 2014-2016
- Tendência de queda após 2016 (possível efeito de dados incompletos)

### 6.2 Análise de Gêneros

**Insight 3: Gêneros Mais Lucrativos**
- **Top 3 gêneros por receita total:**
  1. Action
  2. Adventure
  3. Science Fiction

**Insight 4: ROI por Gênero**
- **Horror** apresenta o melhor ROI médio (baixo orçamento, boa receita)
- **Documentários** têm ROI variável mas geralmente positivo

### 6.3 Análise Financeira

**Insight 5: Relação Orçamento vs Receita**
- Correlação positiva moderada (r ≈ 0.74)
- Filmes de alto orçamento têm maior dispersão de resultados
- Existem outliers: filmes de baixo orçamento com receita altíssima

**Insight 6: Distribuição de Lucro**
- **65%** dos filmes são lucrativos
- **35%** têm prejuízo
- Média de lucro: ~US$ 75 milhões

### 6.4 Dashboards Interativos

Foram criados os seguintes dashboards interativos usando Plotly:

1. **Dashboard Temporal:** Evolução de métricas ao longo do tempo
2. **Dashboard de Gêneros:** Comparação entre gêneros cinematográficos
3. **Dashboard Financeiro:** Análise de orçamento, receita e ROI
4. **Dashboard de Avaliações:** Comportamento das notas de usuários

**Exemplo de Visualização:**
```python
import plotly.express as px

# Gráfico de dispersão: Orçamento vs Receita
fig = px.scatter(
    movies_clean,
    x='budget',
    y='revenue',
    color='roi',
    size='vote_average',
    hover_data=['title', 'release_year'],
    title='Relação entre Orçamento e Receita',
    labels={'budget': 'Orçamento (USD)', 'revenue': 'Receita (USD)'},
    color_continuous_scale='Viridis'
)
fig.show()
```

---

## 7. Conclusões

### 7.1 Resultados Alcançados

Este projeto conseguiu implementar com sucesso um **pipeline completo de Big Data** seguindo as melhores práticas de engenharia de dados. Os principais resultados foram:

1. **Pipeline Funcional:** Implementação completa das etapas de ingestão, transformação, carregamento e visualização
2. **Arquitetura Medallion:** Organização dos dados em camadas Bronze, Silver e Gold
3. **Insights Valiosos:** Identificação de padrões relevantes na indústria cinematográfica
4. **Visualizações Interativas:** Criação de dashboards que facilitam a compreensão dos dados
5. **Documentação Completa:** Código bem documentado e README detalhado

### 7.2 Aprendizados

Durante o desenvolvimento do projeto, a equipe adquiriu conhecimentos práticos sobre:

- **ETL (Extract, Transform, Load):** Processos de extração, limpeza e carregamento de dados
- **Pandas e NumPy:** Manipulação eficiente de grandes volumes de dados
- **Arquitetura de Dados:** Organização em camadas para garantir qualidade progressiva
- **Visualização de Dados:** Criação de gráficos interativos e comunicação de insights
- **Boas Práticas:** Versionamento de código, documentação e reprodutibilidade

### 7.3 Dificuldades Encontradas

1. **Qualidade dos Dados:** O dataset continha muitos valores nulos e inconsistências que exigiram tratamento cuidadoso
2. **Campos JSON Aninhados:** Parse de estruturas complexas (gêneros, produtoras) demandou desenvolvimento de funções auxiliares
3. **Performance:** Processamento de arquivos grandes no Colab exigiu otimizações
4. **Integração de Múltiplas Fontes:** Merge entre movies, credits e ratings apresentou desafios

### 7.4 Considerações Finais

O projeto demonstrou que, mesmo com ferramentas relativamente simples (Python, Pandas, Colab), é possível implementar pipelines de dados robustos e gerar insights valiosos. A arquitetura Medallion se mostrou extremamente útil para organizar o fluxo de dados e garantir rastreabilidade.

A indústria cinematográfica apresenta padrões claros que podem auxiliar na tomada de decisão: gêneros como Action e Adventure são mais lucrativos em termos absolutos, mas Horror oferece melhor ROI; orçamentos altos não garantem sucesso, mas aumentam as chances; e a popularidade (vote_average) tem correlação moderada com receita.

---

## 8. Trabalhos Futuros

### 8.1 Melhorias no Pipeline

1. **Streaming:** Implementar ingestão em tempo real usando ferramentas como Apache Kafka
2. **Escalabilidade:** Migrar para Apache Spark para processar volumes maiores
3. **Automação:** Criar pipelines automatizados com Apache Airflow
4. **Orquestração:** Usar ferramentas de orquestração para agendamento de jobs

### 8.2 Análises Adicionais

1. **Machine Learning:**
   - Modelo de previsão de receita baseado em características do filme
   - Sistema de recomendação de filmes
   - Análise de sentimento em reviews

2. **Análise de Texto:**
   - NLP em sinopses para identificar temas populares
   - Análise de correlação entre palavras-chave e sucesso

3. **Análise de Redes:**
   - Grafo de colaborações entre atores/diretores
   - Identificação de "clusters" de profissionais

### 8.3 Infraestrutura

1. **Cloud:** Migrar para AWS/GCP/Azure para maior poder computacional
2. **Data Warehouse:** Implementar um DW (BigQuery, Redshift, Snowflake)
3. **BI Tools:** Integrar com ferramentas como Tableau ou Power BI
4. **CI/CD:** Implementar pipelines de integração e deploy contínuo


---

## 9. Referências

1. **Dataset:**
   - Kaggle - The Movies Dataset: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

2. **Ferramentas:**
   - Pandas Documentation: https://pandas.pydata.org/docs/
   - Plotly Python: https://plotly.com/python/
   - Google Colab: https://colab.research.google.com/

3. **Conceitos:**
   - Medallion Architecture: Databricks Blog
   - Big Data Pipeline Best Practices
   - ETL vs ELT: Modern Data Pipelines

4. **Fontes de Dados:**
   - TMDB (The Movie Database): https://www.themoviedb.org/

---

## 10. Como Executar

### 10.1 Pré-requisitos

```bash
# Bibliotecas necessárias
pip install pandas numpy plotly pyarrow matplotlib seaborn
```

### 10.2 Executar no Google Colab

1. **Upload do Dataset:**
   - Baixe o dataset do Kaggle
   - Faça upload para o Google Drive
   - Monte o Drive no Colab

2. **Executar o Notebook:**
   - Abra o arquivo `notebooks/movies_pipeline_completo.ipynb`
   - Execute as células sequencialmente
   - Os dados processados serão salvos em `/dados/gold/`

3. **Visualizar Resultados:**
   - Os gráficos aparecerão diretamente no notebook
   - Dashboards interativos podem ser explorados inline

### 10.3 Executar Localmente

```bash
# Clonar o repositório
git clone https://github.com/[seu-usuario]/projeto-bigdata-av2.git
cd projeto-bigdata-av2

# Instalar dependências
pip install -r requirements.txt

# Executar scripts
python src/01_ingestao.py
python src/02_transformacao.py
python src/03_analise.py
python src/04_visualizacao.py

# Ou executar o notebook
jupyter notebook notebooks/movies_pipeline_completo.ipynb
```

### 10.4 Estrutura de Diretórios

```
projeto-bigdata-av2/
├── README.md                          # Este arquivo
├── requirements.txt                   # Dependências Python
├── .gitignore                         # Arquivos ignorados pelo Git
├── dados/
│   ├── bronze/                        # Dados brutos
│   ├── silver/                        # Dados limpos
│   └── gold/                          # Dados refinados
├── notebooks/
│   └── movies_pipeline_completo.ipynb # Notebook principal
├── src/
│   ├── 01_ingestao.py                 # Script de ingestão
│   ├── 02_transformacao.py            # Script de transformação
│   ├── 03_analise.py                  # Script de análises
│   ├── 04_visualizacao.py             # Script de visualizações
│   └── utils.py                       # Funções auxiliares
└── documentacao/
    ├── arquitetura_pipeline.pdf        # Diagrama de arquitetura
    └── apresentacao_final.pdf          # Slides da apresentação
```

---


         
