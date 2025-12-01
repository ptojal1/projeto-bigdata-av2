# Arquitetura do Pipeline de Big Data

## 📐 Visão Geral

Este projeto implementa um **pipeline completo de Big Data** seguindo a **Arquitetura Medallion**, que organiza os dados em três camadas progressivas de refinamento:

- **Bronze** (Raw/Bruto)
- **Silver** (Cleaned/Limpo)
- **Gold** (Refined/Refinado)

---

## 🏗️ Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                         DATA SOURCE                              │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Kaggle: The Movies Dataset                            │    │
│  │  • movies_metadata.csv (~45k filmes)                   │    │
│  │  • credits.csv (elenco/equipe)                         │    │
│  │  • keywords.csv                                        │    │
│  │  • ratings.csv (avaliações)                            │    │
│  └────────────────────────────────────────────────────────┘    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    INGESTION LAYER                               │
│                                                                  │
│  Ferramenta: Kaggle API + Pandas                                │
│  Tipo: Batch (lotes)                                            │
│  Frequência: On-demand                                          │
│                                                                  │
│  Processo:                                                      │
│  1. Download via Kaggle API                                     │
│  2. Descompactação de arquivos                                  │
│  3. Leitura com pandas.read_csv()                               │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     BRONZE LAYER (Raw)                           │
│                                                                  │
│  📁 Localização: /dados/bronze/                                  │
│  📄 Formato: CSV (original)                                      │
│  🔒 Imutável: Dados preservados como recebidos                   │
│                                                                  │
│  Conteúdo:                                                      │
│  • movies_metadata.csv                                          │
│  • credits.csv                                                  │
│  • keywords.csv                                                 │
│  • ratings.csv                                                  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  TRANSFORMATION LAYER                            │
│                                                                  │
│  Ferramenta: Pandas + NumPy + Python                            │
│                                                                  │
│  Transformações:                                                │
│  ✓ Parse de JSON aninhados (genres, companies, etc.)            │
│  ✓ Conversão de tipos de dados                                  │
│  ✓ Tratamento de valores nulos                                  │
│  ✓ Remoção de duplicatas                                        │
│  ✓ Criação de colunas derivadas (ROI, profit, etc.)             │
│  ✓ Filtros de qualidade (status='Released', etc.)               │
│  ✓ Normalização de datas                                        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   SILVER LAYER (Cleaned)                         │
│                                                                  │
│  📁 Localização: /dados/silver/                                  │
│  📄 Formato: Parquet + CSV                                       │
│  ✨ Qualidade: Dados validados e limpos                          │
│                                                                  │
│  Datasets:                                                      │
│  • movies.parquet (filmes processados)                          │
│  • credits.parquet (créditos processados)                       │
│  • keywords.parquet (keywords processadas)                      │
│  • ratings.parquet (avaliações processadas)                     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ANALYTICS LAYER                                │
│                                                                  │
│  Ferramenta: Pandas                                             │
│                                                                  │
│  Processos:                                                     │
│  ✓ Merge de múltiplos datasets                                  │
│  ✓ Agregações (por ano, gênero, diretor)                        │
│  ✓ Cálculos de métricas de negócio                              │
│  ✓ Criação de datasets especializados                           │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    GOLD LAYER (Refined)                          │
│                                                                  │
│  📁 Localização: /dados/gold/                                    │
│  📄 Formato: Parquet + CSV                                       │
│  🎯 Propósito: Pronto para consumo (BI/Analytics)                │
│                                                                  │
│  Datasets:                                                      │
│  • movies_enriched.parquet (dataset completo enriquecido)       │
│  • yearly_analytics.parquet (agregações por ano)                │
│  • genre_analytics.parquet (agregações por gênero)              │
│  • director_analytics.parquet (estatísticas por diretor)        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  VISUALIZATION LAYER                             │
│                                                                  │
│  Ferramentas: Plotly + Matplotlib + Seaborn                     │
│  Ambiente: Jupyter/Colab                                        │
│                                                                  │
│  Outputs:                                                       │
│  📊 Gráficos interativos (Plotly)                                │
│  📈 Dashboards consolidados                                      │
│  💡 Insights e recomendações                                     │
│  📑 Relatórios executivos                                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Componentes Técnicos

### 1. Ingestão de Dados
- **Ferramenta:** Kaggle API
- **Linguagem:** Python
- **Bibliotecas:** `kaggle`, `pandas`
- **Tipo:** Batch processing
- **Destino:** Camada Bronze

### 2. Processamento e Transformação
- **Ferramenta:** Pandas, NumPy
- **Linguagem:** Python
- **Operações:**
  - Parse de JSON (campos aninhados)
  - Type casting (conversão de tipos)
  - Data cleaning (limpeza)
  - Feature engineering (criação de features)
- **Origem:** Bronze
- **Destino:** Silver

### 3. Análise e Agregação
- **Ferramenta:** Pandas
- **Operações:**
  - GroupBy aggregations
  - Joins/Merges
  - Statistical analysis
  - Business metrics calculation
- **Origem:** Silver
- **Destino:** Gold

### 4. Visualização
- **Ferramentas:** Plotly, Matplotlib, Seaborn
- **Tipos de Gráficos:**
  - Line charts (tendências temporais)
  - Bar charts (comparações)
  - Scatter plots (correlações)
  - Histograms (distribuições)
  - Pie charts (proporções)
  - Dashboards multi-gráfico
- **Origem:** Gold

---

## 📊 Fluxo de Dados Detalhado

### Etapa 1: Bronze → Silver (Movies)

```python
# Bronze: CSV bruto
movies_raw = pd.read_csv('bronze/movies_metadata.csv')

# Transformações
1. Parse JSON: genres, production_companies, countries
2. Conversão de tipos: budget, revenue, dates
3. Limpeza: remoção de nulos, duplicatas
4. Validação: status='Released', datas válidas
5. Derivação: profit, ROI, release_year

# Silver: Parquet limpo
movies_clean.to_parquet('silver/movies.parquet')
```

### Etapa 2: Silver → Gold (Enriched)

```python
# Silver: Datasets limpos
movies = pd.read_parquet('silver/movies.parquet')
credits = pd.read_parquet('silver/credits.parquet')
keywords = pd.read_parquet('silver/keywords.parquet')

# Merge
movies_enriched = movies \
    .merge(credits, on='movie_id') \
    .merge(keywords, on='movie_id')

# Gold: Dataset enriquecido
movies_enriched.to_parquet('gold/movies_enriched.parquet')
```

### Etapa 3: Gold → Analytics

```python
# Agregações
yearly_stats = movies_enriched.groupby('release_year').agg({
    'movie_id': 'count',
    'budget': 'mean',
    'revenue': 'mean',
    'roi': 'mean'
})

genre_stats = movies_enriched.groupby('genre').agg({
    'revenue': ['sum', 'mean'],
    'roi': 'mean'
})
```

---

## 🎯 Decisões de Design

### Por que Arquitetura Medallion?

1. **Rastreabilidade:** Bronze preserva dados originais
2. **Qualidade Progressiva:** Cada camada adiciona valor
3. **Flexibilidade:** Fácil re-processar a partir de qualquer camada
4. **Manutenibilidade:** Problemas são fáceis de diagnosticar
5. **Performance:** Gold otimizado para consultas

### Por que Parquet na Silver e Gold?

1. **Compressão:** 70-90% menor que CSV
2. **Performance:** Leitura mais rápida
3. **Schema:** Preserva tipos de dados
4. **Compatibilidade:** Funciona com Pandas, Spark, etc.

### Por que Batch e não Streaming?

1. **Dataset estático:** Dados históricos do Kaggle
2. **Simplicidade:** Batch é mais simples para escopo acadêmico
3. **Custo:** Não requer infraestrutura de streaming
4. **Adequação:** Volume de dados não requer processamento contínuo

---

## 📈 Métricas de Qualidade

### Cobertura de Dados

| Camada | Registros | Completude | Qualidade |
|--------|-----------|------------|-----------|
| Bronze | 45,466 | 100% (raw) | Baixa (muitos nulos) |
| Silver | 44,936 | 98.8% | Alta (validados) |
| Gold | 44,936 | 98.8% | Muito Alta (enriquecidos) |

### Performance

- **Ingestão:** ~2-3 minutos (download Kaggle)
- **Transformação:** ~30-60 segundos
- **Agregação:** ~10-20 segundos
- **Visualização:** Instantânea (dados pré-processados)

---

## 🔒 Boas Práticas Implementadas

✅ Separação clara de camadas (Bronze/Silver/Gold)  
✅ Dados brutos preservados (Bronze imutável)  
✅ Versionamento de código (Git)  
✅ Documentação completa (README, comentários)  
✅ Formato eficiente (Parquet)  
✅ Tratamento de erros (try/except)  
✅ Validação de dados  
✅ Reprodutibilidade (notebooks completos)  

---

## 🚀 Escalabilidade Futura

### Para volumes maiores (10M+ registros):

1. **Spark:** Migrar para PySpark
2. **Cloud:** AWS S3/Glue, GCP BigQuery, Azure Synapse
3. **Streaming:** Kafka + Spark Streaming
4. **Orquestração:** Apache Airflow
5. **Data Warehouse:** Snowflake, Redshift, BigQuery

### Para tempo real:

1. **Ingestão:** Kafka, Kinesis
2. **Processamento:** Spark Streaming, Flink
3. **Storage:** Delta Lake, Iceberg
4. **Analytics:** Druid, ClickHouse

---

## 📚 Referências

- [Databricks - Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
- [Pandas Best Practices](https://pandas.pydata.org/docs/user_guide/index.html)

---

**Última atualização:** Dezembro 2025

