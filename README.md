# Análise de Acervo de Biblioteca

Este projeto realiza a análise de dados de um acervo de biblioteca, extraindo informações importantes como a **contagem de livros por autor** e **contagem de livros por local de publicação**. Além disso, calcula e exibe as **porcentagens** de cada autor e local em relação ao total, e gera gráficos interativos para uma melhor visualização.

## Funcionalidades

1. **Contagem de livros por autor**:
   - Exibe os autores com o maior número de livros no acervo.
   - Exibe as porcentagens de cada autor em relação ao total de livros.

2. **Contagem de livros por local de publicação**:
   - Exibe os locais de publicação com o maior número de livros no acervo.
   - Exibe as porcentagens de cada local em relação ao total de livros.

3. **Geração de Gráficos Interativos**:
   - Utiliza a biblioteca `Plotly` para gerar gráficos de barras interativos.
   - Os gráficos gerados são salvos em formato HTML e são automaticamente abertos no navegador.

## Pré-requisitos

Antes de executar o projeto, você precisa ter o Python e as seguintes bibliotecas instaladas:

- **pandas**: Para manipulação de dados.
- **plotly**: Para a geração de gráficos interativos.
- **matplotlib** (opcional, caso queira gráficos adicionais).

Você pode instalar essas dependências com o seguinte comando:

```bash
pip install pandas plotly
Como Executar
Clone o repositório:
bash
Copiar
git clone https://github.com/seu_usuario/analiselivros.git
Navegue até o diretório do projeto:
bash
Copiar
cd analiselivros
Coloque o arquivo de dados Acervo da Biblioteca - 2024.csv no mesmo diretório ou altere o caminho do arquivo no código.

Execute o script Python:

bash
Copiar
python analisar_acervo.py
O script irá gerar os gráficos interativos e salvá-los como arquivos HTML:
top_10_autores_com_porcentagem.html
top_10_locais_com_porcentagem.html
Esses arquivos HTML serão abertos automaticamente no seu navegador.

Estrutura do Projeto
yaml
Copiar
analiselivros/
│
├── README.md                # Este arquivo
├── analisar_acervo.py       # Script Python para análise e geração de gráficos
└── Acervo da Biblioteca - 2024.csv  # Arquivo CSV contendo os dados do acervo
Exemplo de Saída
Os gráficos gerados terão a seguinte aparência:

Contagem de livros por autor: Gráfico de barras com os 10 autores com maior número de livros, com os valores de livros e suas porcentagens exibidas acima de cada barra.

Contagem de livros por local de publicação: Gráfico de barras com os 10 locais de publicação com maior número de livros, com os valores de livros e suas porcentagens exibidas acima de cada barra.
