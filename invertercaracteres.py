def inverter_string(s):
    """Inverte os caracteres de uma string."""
    # Converte a string em uma lista de caracteres
    lista_caracteres = list(s)
    
    # Define as variáveis de início e fim da lista
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    # Troca os caracteres
    while inicio < fim:
        # Troca os caracteres nas posições 'inicio' e 'fim'
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        # Move os índices
        inicio += 1
        fim -= 1
    
    # Converte a lista de volta para uma string
    return ''.join(lista_caracteres)

# Entrada do usuário
entrada = input("Digite uma string para inverter: ")

# Chama a função e exibe o resultado
print("String invertida:", inverter_string(entrada))
