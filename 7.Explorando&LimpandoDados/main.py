import numpy as np
import pandas as pd
import os

#1.exploração de dados
titanic_train = pd.read_csv(r"C:\Users\Mária\Desktop\praticaAdDPython\train.csv")
#print(titanic_train)

#1.1 checar as dimensões (linha, coluna)
#print(titanic_train.shape)

#1.2 checar os tipos de dados de cada coluna
#print(titanic_train.dtypes)

#1.3 checar valores a partir dos primeiros valores da tabela
#print(titanic_train.head(5))

#1.4 revisão estatística da tabela
#print(titanic_train.describe())

#1.4.1 revisão estatística das variáveis categóricas
#as variáveis categóricas normalmente não são mostradas
#por não serem variáveis numéricas
categorical = titanic_train.dtypes[titanic_train.dtypes == "object"].index
#mostra quais indexes estão dentro da variável
#print(categorical) 
#revisão estatística das variáveis categóricas
#print(titanic_train[categorical].describe())

#2. Avaliar a necessidade das variáveis
#O objetivo da análise do data-set é pre-dizer a quantidade de passageiros sobreviventes

#os dados em PassengerId serão apagados pois servem apenas para identificação
del titanic_train["PassengerId"]

#Variáveis que agrupam de maneira numérica ou categórica, são úteis para a análise
#manter algumas variáveis que possam identicar cada elemento unicamente

del titanic_train["Ticket"] 
#As variáveis PassengerId e Ticket foram retiradas por não
#representarem significância para a análise preditiva

#3. Devo tranformar alguma variável
#modificar algumas variáveis para que os seus elementos estejam mais de 
#acordo com o que essas representam

new_survived = pd.DataFrame(data=titanic_train["Survived"])
print(new_survived)
print(new_survived.describe())
