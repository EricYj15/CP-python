# Análise Exploratória de Incêndios Florestais nos EUA (1992–2020)

**Autor:** [Seu Nome]  
**Data:** [YYYY-MM-DD]

---

## 1. Resumo do Projeto: Objetivo · Contexto · Variáveis

**Objetivo:**  
Realizar análise exploratória dos dados de `wildfires.csv` (1992–2020), identificando padrões de ocorrência (causas, épocas, localização, tamanho) e gerar insights para prevenção e combate via drones e fiscalização remota.

**Contexto:**  
Com o aumento das secas e temperaturas, incêndios florestais se intensificaram. Parte é natural (raios), mas a maioria é humana (queimadas de resíduos, fogueiras descuidadas, arson). Esses padrões auxiliam políticas públicas e tecnologias de vigilância.

**Variáveis da Base de Dados (14 colunas):**  
`FOD_ID`, `FIRE_NAME`, `FIRE_YEAR`, `DISCOVERY_DATE`, `DISCOVERY_DOY`,  
`NWCG_CAUSE_CLASSIFICATION`, `NWCG_GENERAL_CAUSE`, `CONT_DATE`, `CONT_DOY`,  
`FIRE_SIZE`, `FIRE_SIZE_CLASS`, `LATITUDE`, `LONGITUDE`, `STATE`.  
Todas estão presentes após leitura de 2.303.566 registros.

---

## 2. Limpeza e Formatação dos Dados: Datas · Duplicatas · Nulos · Outliers · “Missing”  

- **Datas:**  
  - Convertidas com `pd.to_datetime(…, errors='coerce')` (valores inválidos → `NaT`).

- **Duplicatas:**  
  - `drop_duplicates()`.  
  - Registros de 2.303.566 → 1.705.633 após remoção.

- **Valores Nulos:**  
  - `FIRE_NAME`: 995.415 vazios (mantidos).  
  - `CONT_DATE/CONT_DOY`: 894.813 vazios (mantidos).  
  - Demais colunas essenciais sem nulos pós-filtragem de causas.

- **Outliers (FIRE_SIZE):**  
  - Estatísticas antes de filtrar:  
    - 1%: 0,01 · 5%: 0,10 · 25%: 0,10 · 50%: 0,80 · 75%: 3,00 · 95%: 45,00 · 99%: 477,00 · 100%: 662.700  
  - Mantidos (legítimos; mostram impacto máximo).

- **Filtragem de “Missing”:**  
  - Remoção de registros com `NWCG_GENERAL_CAUSE = “Missing data/not specified/undetermined”`.  
  - `NWCG_CAUSE_CLASSIFICATION` ficou apenas “Human” e “Natural” (sem nulos).  
  - **Dataset final:** 1.705.633 linhas × 14 colunas.

---

## 3. Visualizações e Estatísticas-Chave

Para inserir:  
1. Gráfico 1: Incêndios por Ano  
2. Gráfico 2: Causas Amplas (Human vs. Natural)  
3. Gráfico 3: Top 10 Causas Gerais  
4. Gráfico 4: Localização por Causa Ampla (scatter)  
5. Gráfico 5: DISCOVERY_DOY (sazonalidade)  
6. Gráfico 6: Classe de Tamanho (FIRE_SIZE_CLASS)  
7. Gráfico 7: Boxplot FIRE_SIZE por Causa Ampla (log)

### 3.1 Valores Ausentes (pós limpeza)  
