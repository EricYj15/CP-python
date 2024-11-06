# file = open('notas.txt', 'r')
# for line in file:
#     parts = line.split()
#     nome = parts[0]
#     notas = list(map(int, parts[1:]))
#     nota_minima = min(notas)
#     nota_maxima = max(notas)
#     print(f"{nome} - Nota Mínima: {nota_minima}, Nota Máxima: {nota_maxima}")
# file.close()


# file = open('financeiro.log', 'r')
# saldo = 0

# for line in file:
#     parts = line.split()
#     valor = int(parts[0])
#     saldo += valor

# file.close()

# print(f"Saldo Financeiro: {saldo}")



# valor = input("Digite o valor da transação: ")
# descricao = input("Digite a descrição da transação: ")

# file = open('financeiro.log', 'a')

# file.write(f"{valor} {descricao}\n")

# file.close()

# print("Transação adicionada com sucesso.")



# nome_arquivo = "dados.csv"
# separador = ","

# dados = []

# with open(nome_arquivo, 'r') as file:
#     for line in file:

#         linha = line.strip().split(separador)
#         dados.append(linha)

# print("Conteúdo do arquivo CSV:")
# for linha in dados:
#     print(linha)
