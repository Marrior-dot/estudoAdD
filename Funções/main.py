#passar varias argumentos para uma função
def sum_many_args(*args):
    print (type (args))
    return (sum(args))

    
#print(sum_many_args(1, 2, 3, 4, 5))

#passar os argumentos como chave e valor de dicionário