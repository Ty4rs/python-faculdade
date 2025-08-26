# Criação de uma lista vazia
vet = []

# Criação de uma lista com elementos iniciais
vet2 = [1, 2, 3, 4]

# Adicionando elementos à lista vet2
vet2.append(88)  # Adiciona o número 88 ao final da lista
vet2.append(6)   # Adiciona o número 6 ao final da lista

# Exibindo o conteúdo das listas
print("Conteúdo de vet2:", vet2)  # Mostra todos os elementos de vet2
print("Conteúdo de vet (vazia):", vet)  # Mostra que vet ainda está vazia

# Acessando e exibindo elementos específicos de vet2
print("Primeiro elemento de vet2:", vet2[0])  # Exibe o primeiro elemento
print("Segundo elemento de vet2:", vet2[1])   # Exibe o segundo elemento

type(vet2)  # Verifica o tipo da variável vet2 (deve ser 'list')



vetor = [1, 2, 3, 4, 5, 6, 7] # Criação de uma lista com elementos iniciais
vetor2 = [10, 20, 30, 40, 50, 60, 70] # Criação de uma segunda lista com elementos iniciais
vetor.append(vetor2) # Adiciona a lista vetor2 como um único elemento no final da lista vetor
print(vetor) # Exibe o conteúdo da lista vetor, que agora inclui vetor2 como um sub-lista
print(vetor[7][5]) # Acessa e exibe o sexto elemento da sub-lista vetor2 dentro de vetor (índice 7)


def oi():
    return "oiii"


vetor4 = [1, oi(), oi()]  # Criação de uma lista contendo o retorno da função oi() três vezes
print(vetor4)  # Exibe o conteúdo da lista vetor4, que deve conter três vezes a string "oiii"

def ola():
    print("oii")        

vetor5 = [1, 3, ola]
print(vetor5)  # Exibe o conteúdo da lista vetor5, que inclui a função ola
# Verificando o tipo do primeiro elemento da lista vetor
vetor5[2]()