import pyspark

print("Hello, World!")

# Abrir o arquivo
with open('/C:/Users/01701805/Downloads/Dados_Titulo.txt', 'r', encoding='utf-8') as file:
    # Ler todas as linhas do arquivo
    lines = file.readlines()

# Contar o número de linhas, excluindo a linha do cabeçalho
num_titulos = len(lines) - 1

# Exibir o número de títulos
print(f'Número de títulos: {num_titulos}')