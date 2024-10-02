# Importando bibliotecas
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Configurando o título do aplicativo
st.title('Gerenciamento de Estoque')

# Carregar o CSV
df_produtos = pd.read_csv('estoque.csv', sep=',')

# Converter colunas para numérico
df_produtos['Quantidade'] = pd.to_numeric(df_produtos['Quantidade'], errors='coerce')
df_produtos['Preco'] = pd.to_numeric(df_produtos['Preco'], errors='coerce')

# Calcular total de estoque
df_produtos['Total'] = df_produtos['Preco'] * df_produtos['Quantidade']

# Exibir o DataFrame e os nomes das colunas
st.subheader('Estoque Total:')
st.write(df_produtos)

# Exibir a soma da coluna 'Quantidade'
quantidade_total_estoque = df_produtos['Quantidade'].sum()
st.write(f"Quantidade total em estoque: {quantidade_total_estoque}")

# Agrupando por categoria
media_categoria = df_produtos.groupby(['Categoria']).agg(
    Quantidade_Total=('Quantidade', 'sum'),
    Preco_Total=('Total', 'sum')
).reset_index()

media_quantidade = media_categoria.sort_values(by='Preco_Total', ascending=True)

# Gráfico de barras: Preço Total por Categoria
fig_bar = px.bar(media_quantidade, 
                  x='Categoria', 
                  y='Preco_Total', 
                  title='Preço Total por Categoria',  
                  template='plotly_dark')

st.plotly_chart(fig_bar, key='bar_chart_categoria')

# Exibir estatísticas descritivas
st.subheader('Estatísticas Descritivas')
media = df_produtos['Total'].mean()
mediana = df_produtos['Total'].median()
st.write(f"Média: {media}, Mediana: {mediana}")
st.write('Tendo em vista que a média e mediana são diferentes, a distribuição dos valores não é normal.')
st.write('Abaixo as medidas estatisticas:')
st.write(df_produtos.describe())

# Boxplot de Total por Categoria
fig_box = px.box(df_produtos, x='Categoria', y='Total', title='Boxplot de Total por Categoria')
st.plotly_chart(fig_box, key='box_plot_categoria')
st.write('Com base no boxplot, podemos analisar que os produtos da Categoria Eletrônicos possuem maiores valores que em relação ao outras categorias, o que é justificavel considerando que esses produtos serão mais caros do que produtos alimenticios, vestuario, higiene ou material escolar    ')
st.write('Além disso, sua distribuição possui uma leve assimetria positiva, ou seja, indicando que há maior variabilidade entre os dados com valores maiores que a mediana, os valores mais altos estão puxando a média para cima.')
st.write('O que pode ser justificavel tendo em vista que há uma grande dispersão entre os valores dos produtos dessa categoria ')
st.write('Outro ponto que pode-se observar no boxplot é que na Categoria Higiene temos um outlier, um valor que está além do limite superior')

# Cálculo dos outliers
Q1 = df_produtos['Total'].quantile(0.25)
Q3 = df_produtos['Total'].quantile(0.75)
IQR = Q3 - Q1

ls = Q3 + 1.5 * IQR
li = Q1 - 1.5 * IQR

df_produtos['Outliers'] = np.where((df_produtos['Total'] > ls) | (df_produtos['Total'] < li), True, False)

#Correlação

vestuario = df_produtos[df_produtos['Categoria'] == 'VESTUÁRIO']
if not vestuario.empty:
    fig_scatter = px.scatter(vestuario, x='Quantidade', y='Total', 
                              title='Correlação entre Quantidade e Total em Estoque (Vestuário)',
                              labels={'Quantidade': 'Quantidade de Produtos', 'Total': 'Valor Total em Estoque'})
    st.plotly_chart(fig_scatter, key='scatter_plot_vestuario')

correlacaoTotal = df_produtos['Quantidade'].corr(df_produtos['Total'])
st.write(f"Correlação entre Quantidade e Total: {correlacaoTotal:.2f}")
st.write("É uma correlação inversamente proporcional; quando as quantidades aumentam, o valor do estoque diminui. Isso indica que, na maioria das vezes, há mais produtos com preços menores.")


# Exibir outliers
st.subheader('Outliers')
st.write('Para a seleção de Outliers, primeiro foi realizado o entendimento do tipo de distribuição para entender de que forma seriam selecionados os Outliers')
st.write('Com base em Histograma e tendo em vista que a média e mediana possuiam valores muito discrepantes, foi entendido se tratar de uma distribuição não normal')
st.write('Dessa forma, foi calculado o IQR (Q3 - Q1) para determinar os limites inferior (Q1 - 1.5 * IQR) e superior (Q3 + 1.5 * IQR). Os valores que estavam fora desses limites foram marcados como True para futura identificação.')
st.write(df_produtos[df_produtos['Outliers'] == True])
st.write('Os produtos identificados como Outliers são todos da Categoria Eletrônicos, o que faz sentido tendo em vista que esses produtos possuem valores bem maiores que os demais')

not_outliers = df_produtos[df_produtos['Outliers'] == False]
# Cálculo dos outliers
Q1 = not_outliers['Total'].quantile(0.25)
Q3 = not_outliers['Total'].quantile(0.75)
IQR = Q3 - Q1

ls = Q3 + 1.5 * IQR
li = Q1 - 1.5 * IQR

not_outliers['Outlier'] = np.where((not_outliers['Total'] > ls) | (not_outliers['Total'] < li), True, False)

st.subheader('Outliers - Outra seleção')
st.write('Tendo em vista que os Eletrônicos possuem os maiores valores entre os demais produtos, esses foram retirados da seleção para analisar os possíveis outliers')
st.write('Novamente foi calculado o IQR (Q3 - Q1) para determinar os limites inferior (Q1 - 1.5 * IQR) e superior (Q3 + 1.5 * IQR). Os valores que estavam fora desses limites foram marcados como True para futura identificação.')
st.write(not_outliers[not_outliers['Outlier'] == True])
st.write('Dessa vez, os produtos que caíram na seleção de outliers são o Sapato e Perfume.')
st.write('Conforme análise de correlação, vimos que a quantidade de unidades aumenta enquanto o valor caí para o estoque, o que não é visualizado no caso do Sapato, em relação aos demais produtos de sua mesma categoria, o mesmo possui um valor elevado e uma quantidade elevada no estoque, o que pode ser visto como um erro ao analisar o comportamento do estoque como um todo.')
st.write('No que diz respeito ao perfume, observamos um comportamento distinto em comparação aos outros produtos. Embora este item tenha a menor quantidade em estoque dentro da sua categoria, seu preço elevado de 100 se destaca significativamente, especialmente quando consideramos que os preços típicos dessa categoria variam entre 3 e 25. Essa disparidade de preço sugere que o perfume pode ser inicialmente classificado como um possível outlier. No entanto, ao considerar que ele é um produto premium no mercado e apresenta um valor que, embora elevado, é justificável pela sua qualidade e posicionamento, concluímos que não deve ser tratado como um outlier verdadeiro. Portanto, sua exclusão do grupo de outliers é fundamentada e razoável.')


# Multiselect para categorias
# Multiselect para categorias
st.subheader('Filtrar Produtos por Categoria')
dados = df_produtos.Categoria.unique().tolist()
lista = st.multiselect('Escolha as categorias', dados)

if lista:
    # Filtrar o DataFrame com base nas categorias selecionadas
    df_filtrado = df_produtos[df_produtos['Categoria'].isin(lista)]
    # Exibir gráfico de barras apenas para os produtos filtrados
    st.bar_chart(df_filtrado.set_index('Produto')['Total'])
else:
    st.write("Nenhuma categoria selecionada.")


