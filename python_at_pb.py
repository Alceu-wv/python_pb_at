import sqlite3
import pandas as pd

# ETAPA 3

# Conectar com a base SQLite
conn = sqlite3.connect('tp9.sqlite')

# Carrega a tabela
df = pd.read_csv("AmesHousing.csv")
df.to_sql('housing', conn, if_exists='replace', index=False)

# Carregar os dados em um dataframe desde o banco de dados
df = pd.read_sql_query("SELECT `Lot Area`, Street FROM housing", conn)

print(df[['Lot Area', 'Street']])

# Valores máximo, mínimo e a média da variável numérica
print("Máximo:", df['Lot Area'].max())
print("Mínimo:", df['Lot Area'].min())
print("Média:", df['Lot Area'].mean())

# Listagem de itens únicos da variável categórica
print(df['Street'].unique())

# ETAPA 4

# Lista com os dados da variável numérica
lista_num = df['Lot Area'].tolist()

# Lista com os dados da variável categórica
lista_cat = df['Street'].tolist()

# Soma dos valores acima da média da variável numérica
media = sum(lista_num) / len(lista_num)
soma_valores_acima_media = sum([x for x in lista_num if x > media])
print("Soma dos valores acima da média:", soma_valores_acima_media)

# Função que retorna a contagem de ocorrência dos itens da variável categórica
def contagem_itens(lista):
    return {item: lista.count(item) for item in set(lista)}

print(contagem_itens(lista_cat))

# Finalizando a conexão com o banco de dados
conn.close()
