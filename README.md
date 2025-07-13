# Análise dos Motivos de Cancelamento de Cartão de Crédito

> Projeto de análise de dados que identifica fatores associados ao cancelamento de cartões de crédito, automatizando a geração de relatórios visuais para apoiar estratégias de retenção.

![Demonstração do sistema](https://github.com/vitoriapguimaraes/Python-Cancelamento_Cartao/blob/main/results/AnaliseCancelamentoCartao-Demonstracao.png)

## Funcionalidades Principais

- Limpeza e tratamento automático dos dados (remoção de colunas irrelevantes e valores ausentes)
- Análise exploratória: estatísticas descritivas e distribuição de cancelamentos
- Geração automática de histogramas para todas as variáveis, segmentados por status
- Consolidação dos gráficos em um único PDF para facilitar a análise
- Relatórios prontos para uso por equipes de negócio

## Resultados e Conclusões

- Clientes com menor limite de crédito e alta taxa de utilização tendem a cancelar mais.
- Visualizações revelam padrões úteis para tomada de decisão e retenção de clientes.

## Tecnologias Utilizadas

- Python
- Pandas
- Plotly
- PyPDF2

## Como Executar

1. Clone o repositório:
   ```
   git clone https://github.com/vitoriapguimaraes/Python-Cancelamento_Cartao.git
   ```
2. Instale as dependências:
   ```
   pip install pandas plotly PyPDF2
   ```
3. Execute o projeto:
   ```
   python scripts/app.py
   ```

## Como Usar

- Após a execução, os histogramas e o PDF consolidado serão salvos em `results/HISTOGRAM/`.
- O PDF final será nomeado com a data e hora da execução, por exemplo: `2025-06-06_151425-Histograms.pdf`.
- Analise os histogramas para identificar padrões de cancelamento relacionados a variáveis como limite de crédito, faixa salarial, tempo de cliente, etc.
- O relatório consolidado facilita o compartilhamento dos resultados com equipes de negócio.
- Insights extraídos podem embasar estratégias de retenção e ações preventivas.

## Estrutura de Diretórios

```
/Python-Cancelamento_Cartao
├── scripts/
│   ├── app.py         # Script principal: importa, trata, analisa dados e gera relatórios
│   └── app.ipynb      # Versão notebook para exploração interativa
├── dataset/
│   └── data-bank.csv  # Base de dados dos clientes
├── results/
│   └── HISTOGRAM/     # Histogramas individuais e PDFs consolidados
└── README.md          # Documentação do projeto
```

## Status

✅ Concluído

> Veja as [issues abertas](https://github.com/vitoriapguimaraes/Python-Cancelamento_Cartao/issues) para sugestões de melhorias e próximos passos.

## Mais Sobre Mim

Acesse os arquivos disponíveis na [Pasta Documentos](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
