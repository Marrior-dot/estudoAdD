#---------------------Tuplas----------------------#
tup = 4,5,7
#print(tup[0])
#tup.append(5) não é possível dar append na tupla
tup1 = "foo","ll"

#concatenação de tuplas
print(tup + tup1)

#a, b, c = tup

[a, b, c] = tup

#print(c)
#array de tuplas
seq = [(1,2,3),(4,5,6),(7,8,9)]

#for a, b, c in seq:
#   print('a={0}, b={1}, c={2}'.format(a,b,c))

#*rest serve para representar o resto da tupla que não se quer usar
values = 1,2,3,4,5
a,b, *rest = values
#print(a)
#print(b)
#print(*rest)

a = (1,2,2,2,3,4,2)
#print(a.count(2))
#---------------------Tuplas----------------------#

#---------------------Listas----------------------#
a_list = [2,3,7,None]
tup = ('foo','bar','baz')

#transforma uma tupla em array
b_list = list(tup)

#print(b_list)

#transforma array em tupla
b_list_tuple = tuple(b_list)
#print(b_list_tuple)

#cria um array reordernado a partir da tupla
sorted(b_list_tuple)
#print(b_list_tuple)
#
x = [4, None, 'foo']
x.extend([7, 8, (2,3)])
#print(x)

#enumerate: transforma os valores em tupla, permitindo uma iteração diferente
#for i, value in enumerate(x):
    #print(i, value)

#zip: pareia os valores de arrays e cria uma lista de tuplas
zipped = zip(a_list,x)
print(zipped)

#---------------Dict---------------

my_dict = {"name": "Joe",
           "age": 10, 
           "city": "Paris"}

#retorna as chaves do dicionário
#print(my_dict.keys())
#retorna os valore das chaves do dicionário
#print(my_dict.values())
#retorna os valores das chaves e correspondentes valores em tuplas
#print(my_dict.items())
#---------------Dict---------------

#---------------Set---------------
set1 = {1,3,5,6}
set2 = {1,2,3,4}

#une os dois "sets"
#print(set1.union(set2))

#mostra a intersecção dos dois sets
#print(set1.intersection(set2))

#mostra os elementos que estão set1 mas não estão em set2
#print(set1.difference(set2))

#verifica se todos os elementos de set1 estão presentes em set2
#print(set1.issubset(set2))