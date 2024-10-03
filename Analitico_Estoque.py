import pandas as pd
import matplotlib as plt
import plotly.express as px
import numpy as np

# %%
# Carregar o CSV
df_produtos = pd.read_csv('estoque.csv', sep=',')

# %%
# Exibir o DataFrame e os nomes das colunas
df_produtos.head()

# %%
# Converter a coluna 'Quantidade' para numérico
df_produtos['Quantidade'] = pd.to_numeric(df_produtos['Quantidade'], errors='coerce')
df_produtos['Preco'] = pd.to_numeric(df_produtos['Preco'], errors='coerce')

# %%
# Calcular a soma da coluna 'Quantidade'
quantidade_total_estoque = df_produtos['Quantidade'].sum()
quantidade_total_estoque

# %%
#Quantidade x preço
df_produtos['Total'] = df_produtos['Preco'] * df_produtos['Quantidade']
df_produtos.head()

# %%
media_categoria = df_produtos.groupby(['Categoria']).agg(
    Quantidade_Total = ('Quantidade','sum'),
    Preco_Total = ('Total', 'sum')
    ).reset_index()
media_quantidade = media_categoria.sort_values(by='Preco_Total', ascending=True)


# %%
#Filtra o index
fig = px.bar(media_quantidade, 
             x='Categoria', 
             y='Preco_Total', 
             title='Preço Total por Categoria',  
             template='plotly_dark')

fig.update_xaxes(title_text='Categoria')
fig.update_yaxes(title_text='Preço Total')  

# Exibir o gráfico
fig.show()

# %%
df_produtos.describe()

# %%
fig = px.box(df_produtos,x='Categoria', y='Total')
fig.show()

# %%
Q1 = df_produtos['Total'].quantile(0.25)
Q3 = df_produtos['Total'].quantile(0.75)

IQR = Q3 - Q1

# %%
ls = Q3 + 1.5 * IQR
li = Q3 - 1.5 * IQR

# %%
df_produtos['Outliers'] = np.where((df_produtos['Total'] > ls) | (df_produtos['Total'] < li), True, False)
df_produtos.head(50)

# %%
#Correlação inversamente proporcial, quanto as unidades aumentam, o preço desce
correlacaoTotal = df_produtos['Quantidade'].corr(df_produtos['Total'])
correlacaoTotal

# %%
# Os outliers estão apenas nos eletronicos, o que faz sentido pois normalmente esses são produtos mais caros do que 
# alimenticios ou materiais escolares
df_produtos[df_produtos['Outliers']==True]

# %%
# Identificar outliers em demais categorias

not_outliers = df_produtos[df_produtos['Outliers']==False]

Q1 = not_outliers['Total'].quantile(0.25)
Q3 = not_outliers['Total'].quantile(0.75)

IQR = Q3 - Q1

ls = Q3 + 1.5 * IQR
li = Q3 - 1.5 * IQR

not_outliers.drop('Outliers', axis=1, inplace = True)

not_outliers['Outliers'] = np.where((not_outliers['Total'] > ls) | (not_outliers['Total'] < li), True, False)
not_outliers.head(50)

# %%
not_outliers[not_outliers['Outliers']==True]

# %%
not_outliers[not_outliers['Categoria']=='VESTUÁRIO'].describe()

# %%
vestuario = not_outliers[not_outliers['Categoria']=='VESTUÁRIO']
vestuario

# %%
# Correlação negativa, quando a unidade aumenta o total de estoque diminui e vice-versa
correlacao = vestuario['Quantidade'].corr(vestuario['Total'])
correlacao

# %%
fig = px.scatter(vestuario, x='Quantidade', y='Total', 
                 title='Correlação entre Quantidade e Total em Estoque',
                 labels={'Quantidade': 'Quantidade de Produtos', 'Total': 'Valor Total em Estoque'})
fig.show()

# %%
#O perfume é o unico outlier do grupo, por ser um produto realmente mais caro
higiene = not_outliers[not_outliers['Categoria']=='HIGIENE']
higiene
