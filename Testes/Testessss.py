lista = list()
lista.append(input('Nome: '))
lista.append(input('Idade: '))
arquivo = open("contatos.txt", "a")
arquivo.writelines(lista)
arquivo.close()
arquivo = open("contatos.txt", "r")
lista2 = arquivo.readlines()
for nome in lista2:
    print(nome)
