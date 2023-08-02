#passar varias argumentos para uma função
def sum_many_args(*args):
    print (type (args))
    return (sum(args))

    
#print(sum_many_args(1, 2, 3, 4, 5))

#passar os argumentos como chave e valor de dicionário
def sum_keywords(**kwargs):
    print(kwargs.values())
    print(kwargs.keys())
    print(kwargs.items())

    return (sum(kwargs.values()))

    
#print(sum_keywords(mynum=100, yournum=200))

#função lambda, utilizada para casos de necessidade de funções menores
my_function2 = lambda x, y: x + y

#print(my_function2(5,10))