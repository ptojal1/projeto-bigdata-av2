# 📓 Guia de Uso no Google Colab

## 🚀 Como Executar o Notebook no Colab

### Opção 1: Upload Direto (Mais Rápido)

1. **Acesse o Colab:**
   - Vá em: https://colab.research.google.com/

2. **Upload do Notebook:**
   - Clique em "File" → "Upload notebook"
   - Selecione: `notebooks/movies_pipeline_completo_AV2.ipynb`
   - OU arraste o arquivo para a janela

3. **Pronto!** O notebook está carregado e pronto para executar

---

### Opção 2: Direto do GitHub (Recomendado)

1. **Acesse o Colab:**
   - Vá em: https://colab.research.google.com/

2. **Abrir do GitHub:**
   - Clique em "File" → "Open notebook"
   - Clique na aba "GitHub"
   - Cole a URL: `https://github.com/ptojal1/projeto-bigdata-av2`
   - Selecione o notebook: `notebooks/movies_pipeline_completo_AV2.ipynb`

3. **Link Direto:**
   ```
   https://colab.research.google.com/github/ptojal1/projeto-bigdata-av2/blob/main/notebooks/movies_pipeline_completo_AV2.ipynb
   ```

---

## 📋 Configuração Inicial (Primeira Execução)

### Passo 1: Configurar Kaggle API

O dataset vem do Kaggle, então você precisa de credenciais:

1. **Obter kaggle.json:**
   - Vá em: https://www.kaggle.com/settings
   - Role até "API" section
   - Clique em "Create New API Token"
   - Baixe o arquivo `kaggle.json`

2. **No Colab, execute a célula:**
   ```python
   # Upload do kaggle.json
   from google.colab import files
   uploaded = files.upload()
   
   # Configurar credenciais
   !mkdir -p ~/.kaggle
   !cp kaggle.json ~/.kaggle/
   !chmod 600 ~/.kaggle/kaggle.json
   ```

3. **Faça upload do kaggle.json** quando solicitado

---

## ▶️ Executando o Notebook

### Ordem de Execução:

1. **Seção 1: Configuração** ⚙️
   - Instala dependências (pandas, plotly, etc.)
   - Tempo: ~30 segundos

2. **Seção 2: Ingestion (Bronze)** 📥
   - Baixa dataset do Kaggle (~230 MB)
   - Tempo: ~2-3 minutos

3. **Seção 3: Transformation (Silver)** 🔄
   - Processa e limpa os dados
   - Tempo: ~1 minuto

4. **Seção 4: Analytics (Gold)** 📊
   - Cria datasets agregados
   - Tempo: ~30 segundos

5. **Seção 5: Visualizações Básicas** 📈
   - Gráficos da AV1
   - Tempo: ~10 segundos

6. **Seção 6: Análises Aprofundadas (AV2)** 🔍
   - ROI, Correlações, Diretores, etc.
   - Tempo: ~1 minuto

7. **Seção 7: Dashboard Interativo** 📊
   - Dashboard consolidado
   - Tempo: ~5 segundos

8. **Seção 8: Insights e Conclusões** 💡
   - Resultados finais
   - Tempo: ~5 segundos

**⏱️ Tempo Total: ~5-7 minutos**

---

## 💾 Salvando Resultados (Opcional)

### Opção 1: Montar Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')

# Salvar na pasta do Drive
movies_enriched.to_parquet('/content/drive/MyDrive/bigdata_av2/movies_gold.parquet')
```

### Opção 2: Download Local

```python
from google.colab import files

# Download de arquivos específicos
files.download('data/refined/movies_enriched.parquet')
```

---

## 🔧 Dicas e Truques

### 1. Executar Tudo de Uma Vez
- **Runtime → Run all** (Ctrl+F9)
- Espere ~7 minutos
- Todos os gráficos aparecerão automaticamente

### 2. Reiniciar se Necessário
- **Runtime → Restart runtime**
- Útil se algo der errado

### 3. Ver Uso de Memória
- **Runtime → Manage sessions**
- Colab free tem 12-13 GB RAM (suficiente)

### 4. Modo Escuro
- **Tools → Settings → Theme → Dark**

---

## ⚠️ Problemas Comuns e Soluções

### Problema 1: "Kaggle API not found"
**Solução:** Execute a célula de configuração do Kaggle e faça upload do kaggle.json

### Problema 2: "ModuleNotFoundError"
**Solução:** Execute a primeira célula (instalação de dependências)

### Problema 3: "Out of Memory"
**Solução:** 
- Runtime → Restart runtime
- Ou use Colab Pro (mais RAM)
- Ou reduza o sample nas visualizações

### Problema 4: Dataset muito lento para baixar
**Solução:** 
- Kaggle às vezes é lento
- Aguarde ou tente novamente mais tarde
- Ou use um dataset menor (ratings_small.csv)

---

## 📊 O Que Você Verá

### Gráficos Principais:

1. **Evolução de Produção** - Linha temporal
2. **Top Gêneros** - Barras horizontais
3. **Distribuição de ROI** - Histograma
4. **Orçamento vs Receita** - Scatter log
5. **ROI por Orçamento** - Box plot
6. **Top Diretores** - Barras
7. **Evolução por Década** - Dual-axis
8. **Nota vs Receita** - Scatter
9. **Dashboard Consolidado** - 4 em 1

### Insights Mostrados:

- ✅ ROI mediano da indústria
- ✅ Correlação orçamento-receita (0.74)
- ✅ Melhores gêneros por ROI
- ✅ Tendências temporais
- ✅ Performance por categoria de nota
- ✅ Recomendações estratégicas

---

## 🎬 Para a Apresentação

### Dica 1: Execute Antes
- Execute todo o notebook 1-2 horas antes da apresentação
- Salve uma versão já executada
- Use como backup se a demo ao vivo falhar

### Dica 2: Compartilhe o Link
Adicione ao README do GitHub:
```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ptojal1/projeto-bigdata-av2/blob/main/notebooks/movies_pipeline_completo_AV2.ipynb)
```

### Dica 3: Mostre os Highlights
Na apresentação, foque em:
- Dashboard consolidado (Seção 7)
- Insights principais (Seção 8)
- 1-2 gráficos mais impactantes (ex: Scatter orçamento-receita)

---

## 📱 Atalhos Úteis do Colab

| Ação | Atalho |
|------|--------|
| Executar célula | Ctrl + Enter |
| Executar e ir para próxima | Shift + Enter |
| Executar todas | Ctrl + F9 |
| Adicionar célula acima | Ctrl + M A |
| Adicionar célula abaixo | Ctrl + M B |
| Deletar célula | Ctrl + M D |
| Buscar no código | Ctrl + F |

---

## 🔗 Links Úteis

- **Seu Notebook no Colab:** [Link Direto](https://colab.research.google.com/github/ptojal1/projeto-bigdata-av2/blob/main/notebooks/movies_pipeline_completo_AV2.ipynb)
- **Repositório GitHub:** https://github.com/ptojal1/projeto-bigdata-av2
- **Dataset Original:** https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
- **Kaggle API Docs:** https://github.com/Kaggle/kaggle-api

---

## ✅ Checklist Pré-Apresentação

- [ ] Kaggle.json baixado e pronto
- [ ] Notebook executado do início ao fim (teste)
- [ ] Todos os gráficos apareceram corretamente
- [ ] Tempo total de execução anotado (~7 min)
- [ ] Versão executada salva como backup
- [ ] Link do Colab compartilhado com a equipe
- [ ] Conexão de internet testada

---

**Pronto! Seu notebook está 100% configurado para execução no Google Colab! 🚀**

*Qualquer dúvida, consulte este guia ou execute célula por célula observando os outputs.*

