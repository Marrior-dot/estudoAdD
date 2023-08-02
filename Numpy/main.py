import numpy as np

#numpy apens aceita arrays do mesmo tipo
#numpy pode ser multidimensional

#criando array
my_list = [1,2,3,4]
my_array = np.array(my_list)

#print(type(my_array))

second_list = [5,6,7,8]

#array de duas dimensões
two_d_array = np.array([my_list, second_list])

#print(two_d_array)
#reverter o array
#print(two_d_array[::-1])

#as linhas de cada array
#print(two_d_array[::-1, ::-1])

one_d_array = [1,2,3,4,5,6]
one_d_array = np.array(one_d_array)

#somar os elementos do array
print(np.array([one_d_array, one_d_array+6]))

#concatenar arrays numpy

array_to_join = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(np.concatenate((one_d_array,array_to_join),axis=1)) 