# Camada Silver - Dados Limpos

Esta camada contém dados que passaram por limpeza, validação e transformação inicial.

## Transformações Aplicadas

1. **Limpeza:**
   - Remoção de duplicatas
   - Tratamento de valores nulos
   - Correção de tipos de dados

2. **Normalização:**
   - Conversão de datas para formato datetime
   - Padronização de nomes de colunas
   - Parse de campos JSON aninhados

3. **Validação:**
   - Filtro de registros inválidos
   - Verificação de consistência de dados

## Arquivos

- `movies.parquet` - Filmes processados
- `credits.parquet` - Créditos processados
- `keywords.parquet` - Keywords processadas
- `ratings.parquet` - Avaliações processadas

## Formato

Arquivos salvos em Parquet para melhor compressão e performance.

