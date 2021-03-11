# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1:
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


'''
Escreva uma função com o nome pertence, que recebe como argumentos de
entrada uma tupla e dois itens e retorna True, se os dois itens estiverem
armazenado na tupla, e False, caso contrário.
'''


def pertence(tupla, item1, item2):
    return True if ((item1 in tupla) and (item2 in tupla)) else False


'''
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    for i in range(0, len(lista)):
        if (lista[i] == velho):
            lista[i] = novo
    return lista
    pass


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de
entrada uma lista e um item, e retorna uma tupla contendo todos os índices
em que o item aparece na lista.
'''


def posicoes_lista(lista, item):
    lista1 = []
    for i in range(0, len(lista)):
        if lista[i] == item:
            lista1.append(i)
    return tuple(lista1)


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada reprovados que recebe como argumento de
entrada um dicionário e retorna uma lista com o nome dos alunos reprovados
(um aluno é reprovado quando a média das suas notas é inferior a 6).
'''


def reprovados(alunos):
    lista = []
    for x in alunos:
        total_notas = sum(alunos[x])
        quantidade_notas = len(alunos[x])
        media = total_notas/quantidade_notas
        if media < 6:
            lista.append(x)
    return lista


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''


def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        alunos[nome] += [nota]
    return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada menores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com a
menor nota de cada aluno.
'''


def menores_notas(alunos):
    dicionario = {}
    for x in alunos:
        dicionario[x] = min(alunos[x])
    return dicionario
