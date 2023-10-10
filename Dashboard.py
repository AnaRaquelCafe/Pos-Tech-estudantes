# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Título da aplicação
st.write('# Análise desempenho de estudantes')

# Upload de arquivo com os dados
df = pd.read_csv('StudentsPerformance.csv', sep=';')

df['total score'] = df['math score'] + df['reading score'] + df['writing score']
df['avg score'] = df['total score'] / 3

# Layout do aplicativo
tab0, tab1, tab2, tab3, tab4 = st.tabs(["Geral", "Etnia","Gênero", "Desempenho em notas", "Desempenho por matéria"])

# Separando as Tabs
with tab0:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    """
    ### Desempenho acadêmico de estudantes 
    
    Esta análise explica o desempenho acadêmico pelas variáveis :
    - Gênero
    - Raça
    - Nível acadêmico familiar
    - Refeição
    - Curso preparatório
    - Disciplinas de matemática, leitura e escrita.

    """
    st.write("### Base de dados:")

    #DataFrame
    df_visualizar = pd.DataFrame(df)
    st.dataframe(df_visualizar, use_container_width=True)
    
    plt.rcParams['figure.figsize'] = (30, 12)

    # Create a subplot with five pie charts side by side
    plt.subplot(1, 5, 1)
    size = df['gender'].value_counts()
    labels = 'Female', 'Male'
    color = ['red', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Gender', fontsize=20)
    plt.axis('off')


    plt.subplot(1, 5, 2)
    size = df['race/ethnicity'].value_counts()
    labels = 'Group C', 'Group D', 'Group B', 'Group E', 'Group A'
    color = ['red', 'green', 'blue', 'cyan', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Race/Ethnicity', fontsize=20)
    plt.axis('off')

    plt.subplot(1, 5, 3)
    size = df['lunch'].value_counts()
    labels = 'Standard', 'Free'
    color = ['red', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Lunch', fontsize=20)
    plt.axis('off')

    plt.subplot(1, 5, 4)
    size = df['test preparation course'].value_counts()
    labels = 'None', 'Completed'
    color = ['red', 'orange']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Test Course', fontsize=20)
    plt.axis('off')

    plt.subplot(1, 5, 5)
    size = df['parental level of education'].value_counts()
    labels = 'Some College', "Associate's Degree", 'High School', 'Some High School', "Bachelor's Degree", "Master's Degree"
    color = ['red', 'green', 'blue', 'cyan', 'orange', 'grey']

    plt.pie(size, colors=color, labels=labels, autopct='%.2f%%')
    plt.title('Parental Education', fontsize=20)
    plt.axis('off')

    plt.grid()
    st.pyplot()
    
    
with tab1:
    
    # Título página
    st.write('### Analisando o volume de estudantes por tipo de raça e etinia')

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

with tab2:
    
    # Título da página
    st.write('### Analisando estudantes por gênero')
    
    # Visualização dos dados
    f, ax = plt.subplots(1, 2, figsize=(20, 10))

    sns.countplot(x=df['gender'], data=df, palette='bright', ax=ax[0], saturation=0.95)
    for container in ax[0].containers:
        ax[0].bar_label(container, color='black', size=20)

    plt.pie(x=df['gender'].value_counts(), labels=['Male', 'Female'], explode=[0, 0.1],
            autopct='%1.1f%%', shadow=True, colors=['#ff4d4d', '#ff8000'])
    plt.title('Gender Distribution', fontsize=20)

    st.pyplot(f)
    
    st.write('O gênero predominante na base é o masculino, sendo composto por 51.8% de pessoas')

with tab3:
    # Título da página
    st.write('### Analisando desempenho em notas')
    
    # Visualização dos dados
    fig, ax = plt.subplots(1,2, figsize=(15,7))
    plt.subplot(121)
    sns.histplot(data=df, x='avg score', bins=30, kde=True, color='g')
    plt.subplot(122)
    sns.histplot(data=df, x='avg score', kde=True, hue='gender')
    st.pyplot(fig)
    
        
with tab4:
    # Título da página
    st.write('### Analisando desempenho por matéria')
    
    # Visualização dos dados
    plt.subplots(1,4,figsize=(16,5))
    plt.subplot(141)
    sns.boxplot(df['math score'],color='blue')
    plt.subplot(142)
    sns.boxplot(df['reading score'],color='red')
    plt.subplot(143)
    sns.boxplot(df['writing score'],color='yellow')
    plt.subplot(144)
    sns.boxplot(df['avg score'],color='orange')
    st.pyplot()