import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv('Acervo da Biblioteca - 2024.csv', delimiter=';')  # Ajuste o delimitador conforme necessário
print(df)

# Função para personalizar as cores e o estilo do gráfico
def customize_graph(fig):
    # Definir uma paleta de cores mais forte
    fig.update_traces(marker=dict(color='rgb(0, 153, 255)', line=dict(color='rgb(0, 102, 204)', width=2)))

    # Ajustar o layout para melhorar o design
    fig.update_layout(
        title_font=dict(size=24, color='rgb(0, 51, 102)', family='Arial, sans-serif'),
        xaxis_title_font=dict(size=18, color='rgb(0, 51, 102)', family='Arial, sans-serif'),
        yaxis_title_font=dict(size=18, color='rgb(0, 51, 102)', family='Arial, sans-serif'),
        plot_bgcolor='rgb(245, 245, 245)',  # Fundo claro
        paper_bgcolor='rgb(255, 255, 255)',  # Cor de fundo da página
        font=dict(size=14, color='rgb(51, 51, 51)'),
        margin=dict(l=40, r=40, t=40, b=40),  # Melhorar as margens
        showlegend=False
    )
    return fig


# 1. Contagem de livros por melhores autores (top 10 autores)
if 'author' in df.columns:
    autor_count = df['author'].value_counts().reset_index()
    autor_count.columns = ['Autor', 'Número de Livros']

    # Selecionar os top 10 autores com maior número de livros
    top_autores = autor_count.head(10)

    # Calcular a porcentagem de cada autor
    total_livros = top_autores['Número de Livros'].sum()
    top_autores['Porcentagem'] = (top_autores['Número de Livros'] / total_livros) * 100

    fig = px.bar(top_autores, x='Autor', y='Número de Livros',
                 title='Top 10 Autores com Maior Número de Livros',
                 labels={'Autor': 'Autor', 'Número de Livros': 'Número de Livros'})

    # Adicionar as porcentagens acima das barras
    fig.update_traces(text=top_autores['Porcentagem'].round(2).astype(str) + '%',
                      textposition='outside',
                      textfont=dict(size=14, color='black'))

    fig = customize_graph(fig)
    fig.write_html('top_10_autores_com_porcentagem.html', auto_open=True)
    print(
        "Gráfico de Contagem de Livros pelos Melhores Autores com Porcentagem gerado em 'top_10_autores_com_porcentagem.html'.")

# 2. Contagem de livros por melhores locais de publicação (top 10 locais)
if 'place' in df.columns:
    local_count = df['place'].value_counts().reset_index()
    local_count.columns = ['Local', 'Número de Livros']

    # Selecionar os top 10 locais com maior número de livros
    top_locais = local_count.head(10)

    # Calcular a porcentagem de cada local
    total_livros_locais = top_locais['Número de Livros'].sum()
    top_locais['Porcentagem'] = (top_locais['Número de Livros'] / total_livros_locais) * 100

    fig = px.bar(top_locais, x='Local', y='Número de Livros',
                 title='Top 10 Locais de Publicação com Maior Número de Livros',
                 labels={'Local': 'Local', 'Número de Livros': 'Número de Livros'})

    # Adicionar as porcentagens acima das barras
    fig.update_traces(text=top_locais['Porcentagem'].round(2).astype(str) + '%',
                      textposition='outside',
                      textfont=dict(size=14, color='black'))

    fig = customize_graph(fig)
    fig.write_html('top_10_locais_com_porcentagem.html', auto_open=True)
    print(
        "Gráfico de Contagem de Livros pelos Melhores Locais com Porcentagem gerado em 'top_10_locais_com_porcentagem.html'.")
