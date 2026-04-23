
import json
import pandas as pd

file = open('data/vendas.json')

data = json.load(file)
#print (data)

df = pd.DataFrame.from_dict(data)
#formata a coluna 'Data da Compra' para o tipo datetime, utilizando o formato específico de dia/mês/ano. Isso permite realizar operações de data posteriormente, como agrupamento por mês ou ano.
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y') #%y -> ano com dois dígitos, %Y -> ano com quatro dígitos

#print(df)
file.close()