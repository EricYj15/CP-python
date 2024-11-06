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



# import pickle
# try:
#     cadastro = pickle.load(open("cadastro.bin", "rb"))
#     menuPrincipal(cadastro)
#     print("\nSalvando cadastro...")
#     pickle.dump(cadastro,open("cadastro.bin", "wb"))
# except FileNotFoundError:
#     print("Criando cadastro...")
#     cadastro = []
#     menuPrincipal(cadastro)
#     pickle.dump(cadastro,open("cadastro.bin", "wb"))
# except IOError:
#     print("Problemas no arquivo de cadastro.")


# import pickle
# try:
#     arquivo = open("teste.bin", "rb")
#     l = pickle.load(arquivo)
#     print(l)
#     arquivo.close()
# except:
#     print("Problemas com o arquivo.")




# arquivo = open('troca.txt', 'r')
# conteudo = arquivo.read()
# arquivo.close()

# conteudo_modificado = conteudo.replace('a', 'A')

# arquivo = open('troca.txt', 'w')
# arquivo.write(conteudo_modificado)
# arquivo.close()
# print("Texto alterado com sucesso!")
