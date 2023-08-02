import pandas as pd
import numpy as np

my_series = pd.Series(data=[2,3,5,4],
                      index=['a','b','c','d'])
#series no pandas funcionam como se fossem tabelas
#print(my_series)

#passar um dicionário como serie no 
my_dict = {"a":2, "b":3, "c":4, "d":5}
my_series_two=pd.Series(my_dict)

#print(my_series_two)


#dataFrame
data = {
    'state':['ohio', 'ohio', 'ohio', 'nevada', 'nevada', 'nevada']
    , 'year':[2000,2001,2002,2001,2002,2003]
    , 'pop':[1.5,1.7,3.6,2.4,2.9,3.2]
}

frame = pd.DataFrame(data) 
#print(frame)

#estabelecer a ordem das colunas
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
#print(frame)

#imprimir coluna com valor ausente
frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'dept'])
#print(frame)

#nomeando o index
frame = pd.DataFrame(data, columns=['year', 'state', 'pop', 'dept'], index=['one','two','three','four','five','six'])
#print(frame)

#print(frame.year)
#print(frame['year'])

#deletando uma coluna
#del frame['year']

#print(frame)
#somente os valores das colunas
#print(frame.values)

#reindexação de dataFrame
reindex_frame = frame.reindex(['1','2','3','4','5','6'])
#print(reindex_frame)

#O método loc funcionda seguinte forma: loc[linhas(index), coluna]
#print(frame.loc[['one', 'two', 'three'], 'year'])

#caso o index não tenha sido atribuido com outros nomes usar iloc