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