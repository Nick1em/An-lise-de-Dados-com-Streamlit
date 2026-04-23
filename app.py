import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mesnsal,grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores, grafico_vendas_vendedores

st.set_page_config(layout="wide") # Configura o layout para ocupar toda a largura da página
st.title("Dashboard de Vendas :shopping_cart: ") #:shopping_cart: -> coloca emoji de carrinho de compras


##Barra lateral para filtro de vendedores
st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
)

if filtro_vendedor:
        df = df[df['Vendedor'].isin(filtro_vendedor)]

aba1, aba2,aba3 = st.tabs(['Dataset', 'Receita','Vendedores']) # Cria as abas para o dashboard

with aba1:
    st.dataframe(df) # Exibe o dataset na primeira aba Dataset

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total',format_number(df ['Preço'].sum(), 'R$'))# Exibe a receita total calculada a partir da soma da coluna 'Preço' do dataset
        st.plotly_chart(grafico_map_estado, use_container_width=True) # Exibe o gráfico de receita por estado utilizando o gráfico criado em graficos.py    
        st.plotly_chart(grafico_rec_estado, use_container_width=True) # Exibe o gráfico de receita por estado utilizando o gráfico criado em graficos.py 


    with coluna2:
        st.metric('Quantidade de Venddas', format_number(df.shape[0])) # Exibe a quantidade de vendas calculada a partir do número de linhas do dataset
        st.plotly_chart(grafico_rec_mesnsal, use_container_width=True) # Exibe o gráfico de receita mensal utilizando o gráfico criado em graficos.py   
        st.plotly_chart(grafico_rec_categoria, use_container_width=True) # Exibe o gráfico de receita por categoria utilizando o gráfico criado em graficos.py 

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores) # Exibe o gráfico de receita por vendedor utilizando o gráfico criado em graficos.py
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores) # Exibe o gráfico de quantidade de vendas por vendedor utilizando o gráfico criado em graficos.py





