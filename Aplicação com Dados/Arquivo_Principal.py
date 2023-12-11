# Grupo 4

# Equipe:
# Ana Julia de Medeiros Leite
# Isaque Felipe Ponciano de Menezes
# Laura Kelly Pereira Costa


import json
import matplotlib.pyplot as plt

with open("listagem-de-filmes-brasileiros-lancados-1995-a-2021-3.json", "r", encoding="UTF-8") as arq:
    base = json.load(arq)


# 1 - Quantidade de filmes produzidos em 2007 de cada gênero?
def producao(base):
    filmes = {}
    for linhas in base:
        ano = linhas["Ano de Lançamento"]
        genero = linhas["Gênero"]
        if len(ano) == 4:
            ano = int(ano)
            if ano == 2007:
                if genero in filmes:
                    filmes[genero] += 1
                else:
                    filmes[genero] = 1
    return filmes


# 2 - Qual a quantidade de filmes produzidos por ano?
def quantidade(base):
    filmes = {}
    for linhas in base:
        ano = linhas["Ano de Lançamento"]
        if len(ano) == 4:
            ano = int(ano)
            if 1995 <= ano <= 2021:
                if ano in filmes:
                    filmes[ano] += 1
                else:
                    filmes[ano] = 1
    return filmes


# 3 - Qual o principal gênero de filme exibido em Minas Gerais?
def exibicao(base):
    exb = {}
    for linhas in base:
        unidade_federativa = linhas["UF"]
        genero = linhas["Gênero"]
        unidade_federativa = unidade_federativa[:2]
        if unidade_federativa == "MG":
            if genero in exb:
                exb[genero] += 1
            else:
                exb[genero] = 1

    return exb


# 4 - Quais estados possuem a maior quantidade de exibição de filmes?
def ufs(base):
    uf = {}
    for linhas in base:
        unidade_federativa = linhas["UF"]
        unidade_federativa = unidade_federativa[:2]
        if "-" in unidade_federativa:
            unidade_federativa = "Sem Est."

        if unidade_federativa in uf:
            uf[unidade_federativa] += 1
        else:
            uf[unidade_federativa] = 1

    return uf


# 5 - Quais as distribuidoras que mais distribuíram filmes?
def distribuidoras(base):
    distri = {}
    for linhas in base:
        distribuidora = linhas["Distribuidora"]
        if distribuidora in distri:
            distri[distribuidora] += 1
        else:
            distri[distribuidora] = 1
    excluir = []
    for X, Y in distri.items():
        f'{X}{Y}'
        if Y <= 45:
            excluir.append(X)
    for c in range(len(excluir)):
        distri.pop(excluir[c])

    return distri


# ----------------------------------------------------------------------------


# Grafico da Questão 1:


resultado = producao(base)


X = resultado.keys()
Y = resultado.values()

plt.bar(X, Y, width=0.8)
plt.title('Grafico da Questão 1', fontsize=20)
plt.ylabel('Quantidade de Filmes', fontsize=15)
plt.xlabel('Gêneros', fontsize=15)
plt.show()


# Grafico da Questão 2:


resultado2 = quantidade(base)


X = resultado2.keys()
posicao_anos = list(range(len(X)))
Y = resultado2.values()

plt.plot(Y, linewidth=4.0, c='g', marker='o')
plt.xticks(posicao_anos, X, fontsize = 8)
plt.title('Grafico da Questão 2', fontsize=18)
plt.xlabel('Anos', fontsize=15)
plt.ylabel('Total de Filmes Produzidos', fontsize=15)
plt.show()


# Grafico da Questão 3:


resultado3 = exibicao(base)


X = resultado3.keys()
Y = resultado3.values()


plt.pie(Y, labels = X)
plt.legend(title='Quant. de Filmes', labels = Y)
plt.title('Grafico da Questão 3', fontsize=18)
plt.show()


# Grafico da Questão 4:


resultado4 = ufs(base)


X = resultado4.keys()
Y = resultado4.values()

plt.bar(X, Y, width=0.8)
plt.title('Grafico da Questão 4', fontsize=20)
plt.ylabel('Quantidade de Exibação de Filmes', fontsize=15)
plt.xlabel('Estados', fontsize=13)
plt.xticks(rotation = 35, fontsize = 9)
plt.show()


# Grafico da Questão 5:


resultado5 = distribuidoras(base)


X = resultado5.keys()
Y = resultado5.values()


plt.pie(Y, labels = X)
plt.legend(title='Quantidade de Distribuidora', labels = Y, loc='upper right', bbox_to_anchor=(1.5, 1))
plt.title('Grafico da Questão 5', fontsize=18)
plt.show()