import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.write('# Dashboard análise desempenho de estudantes')

# Upload de arquivo com os dados
df = pd.read_csv('StudentsPerformance.csv', sep=';')

#DataFrame
df_visualizar = pd.DataFrame(df)
# st.dataframe(df_visualizar, use_container_width=True)

st.write('Analisando o volume de estudantes por tipo de raça e etinia')
# Visualização dos dados
f, ax = plt.subplots(1, 2, figsize=(20, 10))

sns.countplot(x=df['race/ethnicity'], data=df, palette='bright', ax=ax[0], saturation=0.95)
for container in ax[0].containers:
    ax[0].bar_label(container, color='black', size=20)

plt.pie(x=df['race/ethnicity'].value_counts(), labels=df['race/ethnicity'].value_counts().index,
        explode=[0.1, 0, 0, 0, 0], autopct='%1.1f%%', shadow=True)
plt.title('Race/Ethnicity Distribution', fontsize=20)

st.pyplot(f)

st.write('Com o gráfico é possível analisar que o maior grupo de estudantes é o grupo C que compõe 31.9% do total de estudantes.')
