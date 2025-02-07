# Função para verificar se uma palavra é um palíndromo
def eh_palindromo(palavra):
    """
    Esta função verifica se uma palavra é um palíndromo.
    
    Parâmetros:
    palavra (str): A palavra a ser verificada.
    
    Retorna:
    bool: True se a palavra for um palíndromo, False caso contrário.
    """
    # Converte a palavra para minúsculas para garantir que a verificação seja case-insensitive
    palavra = palavra.lower()
    
    # Inverte a palavra usando slicing
    palavra_invertida = palavra[::-1]
    
    # Compara a palavra original com a palavra invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False

# TODO: Solicitar ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# TODO: Chamar a função eh_palindromo com a palavra fornecida pelo usuário e armazenar o resultado
resultado = eh_palindromo(palavra)

# TODO: Exibir o resultado para o usuário
if resultado:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")