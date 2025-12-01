"""
Funções Utilitárias para o Pipeline de Big Data - Análise de Filmes
Autor: Equipe Big Data
Data: Dezembro 2025
"""

import pandas as pd
import numpy as np
import json
from typing import List, Dict, Any
import warnings
warnings.filterwarnings('ignore')


def parse_json_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Faz o parse de uma coluna que contém JSON string para extrair informações
    
    Args:
        df: DataFrame contendo a coluna
        column: Nome da coluna com JSON
        
    Returns:
        DataFrame com a coluna parseada
    """
    def safe_parse(x):
        try:
            if pd.isna(x):
                return []
            if isinstance(x, str):
                return json.loads(x.replace("'", '"'))
            return x
        except:
            return []
    
    df[column] = df[column].apply(safe_parse)
    return df


def extract_first_item_name(json_list: List[Dict]) -> str:
    """
    Extrai o nome do primeiro item de uma lista JSON
    
    Args:
        json_list: Lista de dicionários JSON
        
    Returns:
        Nome do primeiro item ou string vazia
    """
    if isinstance(json_list, list) and len(json_list) > 0:
        return json_list[0].get('name', '')
    return ''


def extract_all_names(json_list: List[Dict]) -> List[str]:
    """
    Extrai todos os nomes de uma lista JSON
    
    Args:
        json_list: Lista de dicionários JSON
        
    Returns:
        Lista de nomes
    """
    if isinstance(json_list, list):
        return [item.get('name', '') for item in json_list if 'name' in item]
    return []


def calculate_roi(revenue: float, budget: float) -> float:
    """
    Calcula o ROI (Return on Investment) em percentual
    
    Args:
        revenue: Receita do filme
        budget: Orçamento do filme
        
    Returns:
        ROI em percentual ou NaN se orçamento for 0
    """
    if budget > 0:
        return ((revenue / budget) - 1) * 100
    return np.nan


def categorize_budget(budget: float) -> str:
    """
    Categoriza o orçamento em Low, Medium ou High
    
    Args:
        budget: Valor do orçamento
        
    Returns:
        Categoria do orçamento
    """
    if pd.isna(budget) or budget == 0:
        return 'Unknown'
    elif budget < 5_000_000:
        return 'Low'
    elif budget < 50_000_000:
        return 'Medium'
    else:
        return 'High'


def clean_numeric_column(series: pd.Series) -> pd.Series:
    """
    Limpa uma coluna numérica, convertendo strings e tratando erros
    
    Args:
        series: Série pandas a ser limpa
        
    Returns:
        Série limpa
    """
    return pd.to_numeric(series, errors='coerce')


def clean_date_column(series: pd.Series) -> pd.Series:
    """
    Limpa uma coluna de datas, convertendo strings e tratando erros
    
    Args:
        series: Série pandas a ser limpa
        
    Returns:
        Série limpa com datas
    """
    return pd.to_datetime(series, errors='coerce')


def remove_outliers_iqr(df: pd.DataFrame, column: str, threshold: float = 1.5) -> pd.DataFrame:
    """
    Remove outliers usando o método IQR (Interquartile Range)
    
    Args:
        df: DataFrame
        column: Nome da coluna para remover outliers
        threshold: Multiplicador do IQR (padrão 1.5)
        
    Returns:
        DataFrame sem outliers
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


def get_top_n(df: pd.DataFrame, column: str, n: int = 10, ascending: bool = False) -> pd.DataFrame:
    """
    Retorna os top N registros ordenados por uma coluna
    
    Args:
        df: DataFrame
        column: Coluna para ordenação
        n: Número de registros a retornar
        ascending: Ordem crescente (True) ou decrescente (False)
        
    Returns:
        DataFrame com top N registros
    """
    return df.nlargest(n, column) if not ascending else df.nsmallest(n, column)


def create_decade_column(year_series: pd.Series) -> pd.Series:
    """
    Cria uma coluna de década a partir de uma série de anos
    
    Args:
        year_series: Série com anos
        
    Returns:
        Série com décadas
    """
    return (year_series // 10) * 10


def print_dataset_info(df: pd.DataFrame, dataset_name: str = "Dataset"):
    """
    Imprime informações resumidas sobre um dataset
    
    Args:
        df: DataFrame
        dataset_name: Nome do dataset para exibição
    """
    print(f"\n{'='*60}")
    print(f"📊 Informações do {dataset_name}")
    print(f"{'='*60}")
    print(f"Número de registros: {len(df):,}")
    print(f"Número de colunas: {len(df.columns)}")
    print(f"Memória utilizada: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print(f"\n📋 Colunas:")
    for col in df.columns:
        null_pct = (df[col].isna().sum() / len(df)) * 100
        print(f"  - {col}: {df[col].dtype} (Nulos: {null_pct:.1f}%)")
    print(f"{'='*60}\n")


def save_to_bronze(df: pd.DataFrame, filename: str, path: str = '../dados/bronze/'):
    """
    Salva DataFrame na camada Bronze (dados brutos)
    
    Args:
        df: DataFrame a ser salvo
        filename: Nome do arquivo (sem extensão)
        path: Caminho do diretório bronze
    """
    csv_path = f"{path}{filename}.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Dados salvos na camada BRONZE: {csv_path}")


def save_to_silver(df: pd.DataFrame, filename: str, path: str = '../dados/silver/'):
    """
    Salva DataFrame na camada Silver (dados limpos)
    
    Args:
        df: DataFrame a ser salvo
        filename: Nome do arquivo (sem extensão)
        path: Caminho do diretório silver
    """
    csv_path = f"{path}{filename}.csv"
    parquet_path = f"{path}{filename}.parquet"
    
    df.to_csv(csv_path, index=False)
    df.to_parquet(parquet_path, index=False)
    print(f"✅ Dados salvos na camada SILVER:")
    print(f"   - CSV: {csv_path}")
    print(f"   - Parquet: {parquet_path}")


def save_to_gold(df: pd.DataFrame, filename: str, path: str = '../dados/gold/'):
    """
    Salva DataFrame na camada Gold (dados refinados)
    
    Args:
        df: DataFrame a ser salvo
        filename: Nome do arquivo (sem extensão)
        path: Caminho do diretório gold
    """
    csv_path = f"{path}{filename}.csv"
    parquet_path = f"{path}{filename}.parquet"
    
    df.to_csv(csv_path, index=False)
    df.to_parquet(parquet_path, index=False)
    print(f"✅ Dados salvos na camada GOLD:")
    print(f"   - CSV: {csv_path}")
    print(f"   - Parquet: {parquet_path}")


def load_from_bronze(filename: str, path: str = '../dados/bronze/') -> pd.DataFrame:
    """
    Carrega DataFrame da camada Bronze
    
    Args:
        filename: Nome do arquivo (com extensão)
        path: Caminho do diretório bronze
        
    Returns:
        DataFrame carregado
    """
    file_path = f"{path}{filename}"
    print(f"📂 Carregando dados da camada BRONZE: {file_path}")
    return pd.read_csv(file_path, low_memory=False)


def load_from_silver(filename: str, path: str = '../dados/silver/', use_parquet: bool = True) -> pd.DataFrame:
    """
    Carrega DataFrame da camada Silver
    
    Args:
        filename: Nome do arquivo (sem extensão)
        path: Caminho do diretório silver
        use_parquet: Se True, carrega .parquet; se False, carrega .csv
        
    Returns:
        DataFrame carregado
    """
    if use_parquet:
        file_path = f"{path}{filename}.parquet"
        print(f"📂 Carregando dados da camada SILVER: {file_path}")
        return pd.read_parquet(file_path)
    else:
        file_path = f"{path}{filename}.csv"
        print(f"📂 Carregando dados da camada SILVER: {file_path}")
        return pd.read_csv(file_path, low_memory=False)


def load_from_gold(filename: str, path: str = '../dados/gold/', use_parquet: bool = True) -> pd.DataFrame:
    """
    Carrega DataFrame da camada Gold
    
    Args:
        filename: Nome do arquivo (sem extensão)
        path: Caminho do diretório gold
        use_parquet: Se True, carrega .parquet; se False, carrega .csv
        
    Returns:
        DataFrame carregado
    """
    if use_parquet:
        file_path = f"{path}{filename}.parquet"
        print(f"📂 Carregando dados da camada GOLD: {file_path}")
        return pd.read_parquet(file_path)
    else:
        file_path = f"{path}{filename}.csv"
        print(f"📂 Carregando dados da camada GOLD: {file_path}")
        return pd.read_csv(file_path, low_memory=False)


if __name__ == "__main__":
    print("🛠️  Módulo de utilidades carregado com sucesso!")
    print("Funções disponíveis:")
    print("  - parse_json_column()")
    print("  - extract_first_item_name()")
    print("  - extract_all_names()")
    print("  - calculate_roi()")
    print("  - categorize_budget()")
    print("  - clean_numeric_column()")
    print("  - clean_date_column()")
    print("  - remove_outliers_iqr()")
    print("  - get_top_n()")
    print("  - create_decade_column()")
    print("  - print_dataset_info()")
    print("  - save_to_bronze/silver/gold()")
    print("  - load_from_bronze/silver/gold()")

