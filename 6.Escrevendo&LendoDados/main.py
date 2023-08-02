import numpy as np
import pandas as pd
import os

#saber o diretório atual
#print(os.getcwd())

#mudar o diretório atual
os.chdir(r"C:\Users\Mária\Desktop\praticaAdDPython")
#print(os.getcwd())

#listar o que está dentro do diretório atual
#print(os.listdir())

#ler arquivo csv
titanic_train = pd.read_csv(r"C:\Users\Mária\Desktop\praticaAdDPython\train.csv")
#6 primeiras linhas do arquivo csv
#print(titanic_train.head(6))

#ler arquivo excel, precisa de uma extensão especifica
draft = pd.read_excel(r"C:\Users\Mária\Desktop\praticaAdDPython\draft2015.xlsx", sheet_name='draft2015')
#print(draft.head(6))


#transforma outros arquivos em csv b 
draft.to_csv("draft.csv")
