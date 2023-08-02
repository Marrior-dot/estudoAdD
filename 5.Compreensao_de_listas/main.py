#usando o for dentro de listas
my_list2 = [number for number in range(0, 101)]

#print(my_list2)

#utilizando condicionais para inserir os elementos dentro da lista
my_list3 = [number for number in range(0, 101) if number % 2 == 0]

#print(my_list3)


#nested for, nesse caso é feita uma espécie de produto cartesiano entre os caracteres dos strings
combined = [a + b  for a in "life" for b in "study"]

#print (combined)

#exemplo ruim de operação de loop com uma lista dentro de outra lista
#legibilidade ruim
nested = [letters[1] for letters in [a + b  for a in "life" for b in "study"]]

#print(nested)

#exemplo bom de operação de loop com uma lista dentro de outra lista
#boa legibilidade
combined = [a + b  for a in "life" for b in "study"]
non_nested = [letters[1] for letters in combined]

#print (non_nested)

#----------------Dicionário---------------------
words = ["life","is","study"]

#atribuir o valor do dicionário de maneira semelhante
#no código a seguir, para cada word presente em words
#os itens no dicionário serão inseridos da seguinte forma 
#"word": len(word)
word_length_dict2 = {word:len(word) for word in words}

print(word_length_dict2)
