# Análise dos Motivos de Cancelamento de Cartão de Crédito

> Projeto de análise de dados para identificar fatores associados ao cancelamento de cartões de crédito, com geração automática de relatórios visuais e insights para retenção de clientes.

Este projeto utiliza uma base de dados real de clientes para investigar os principais motivos que levam ao cancelamento de cartões de crédito. A análise envolve limpeza de dados, exploração estatística e visualização, permitindo identificar padrões e propor estratégias para reduzir a evasão de clientes.

O diferencial está na automação: o script gera histogramas segmentados por status de cancelamento para todas as variáveis relevantes, salvando-os em PDF e consolidando tudo em um relatório único, pronto para análise e compartilhamento.

Os resultados incluem histogramas em PDF, mostrando a relação entre variáveis como renda, limite de crédito e status do cliente (ativo ou cancelado). Um PDF consolidado reúne todos os gráficos para facilitar a análise.

![Resultado do sistema](https://github.com/vitoriapguimaraes/Python-Cancelamento_Cartao/blob/main/results/AnaliseCancelamentoCartao-Demonstracao.png)

## Funcionalidades Principais

- Limpeza e tratamento automático dos dados (remoção de colunas irrelevantes e valores ausentes)
- Análise exploratória: estatísticas descritivas e distribuição de cancelamentos
- Geração automática de histogramas para todas as variáveis, segmentados por status
- Consolidação dos gráficos em um único PDF para facilitar a análise
- Relatórios prontos para uso por equipes de negócio

## Tecnologias Utilizadas

- **Python**: linguagem principal
- **Pandas**: manipulação e análise de dados
- **Plotly**: visualização gráfica interativa e exportação de gráficos
- **PyPDF2**: manipulação e consolidação de arquivos PDF

## Estrutura do Projeto

```
├── scripts/
│   ├── app.py         # Script principal: importa, trata, analisa dados e gera relatórios
│   └── app.ipynb      # Versão notebook para exploração interativa
├── dataset/
│   └── data-bank.csv  # Base de dados dos clientes
├── results/
│   └── HISTOGRAM/     # Histogramas individuais e PDFs consolidados
└── README.md          # Documentação do projeto
```

## Como Executar

### Pré-requisitos

- Python >= 3.7
- Instale as dependências:
  ```
  pip install pandas plotly PyPDF2
  ```

### Passos

1. Execute o script principal:
   ```
   python scripts/app.py
   ```
2. Os histogramas e o PDF consolidado serão salvos em `results/HISTOGRAM/`.
   - O PDF final será nomeado com a data e hora da execução, por exemplo: `2025-06-06_151425-Histograms.pdf`.

## Como Usar e Interpretar

- Analise os histogramas para identificar padrões de cancelamento relacionados a variáveis como limite de crédito, faixa salarial, tempo de cliente, etc.
- O relatório consolidado facilita o compartilhamento dos resultados com equipes de negócio.
- Insights extraídos podem embasar estratégias de retenção e ações preventivas.

## Resultados e Conclusões

- Clientes com menor limite de crédito e alta taxa de utilização tendem a cancelar mais.
- Visualizações revelam padrões úteis para tomada de decisão e retenção de clientes.

## Status

✅ Concluído

> Melhorias a serem incluídas:
> - Adicionar análise preditiva com machine learning para prever cancelamentos
> - - Incorporar gráficos interativos no notebook ou we
>   - - Permitir seleção dinâmica do diretório de entrada

## Mais sobre mim
Acesse os arquivos disponíveis na [Pasta Documentos](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
