class Palavra():
    def __init__(self, sintaxe, classificacao, genero = "masculino"):
        self.sintaxe = sintaxe
        self.classificacao = classificacao
        self.genero = genero

class Expressoes():
    def __init__(self, sintaxe, genero, classificacao = "expressao"):
        self.sintaxe = sintaxe
        self.genero = genero
        self.classificacao = classificacao
        

dicionarioPalavras = []
dicionarioExpressoes = []

dicionarioPalavras.append(Palavra("cachorro", "substantivo"))
dicionarioPalavras.append(Palavra("trabalhar", "verbo"))
dicionarioPalavras.append(Palavra("fazer", "verbo"))
dicionarioPalavras.append(Palavra("família", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("documento", "substantivo"))
dicionarioPalavras.append(Palavra("homem", "substantivo"))
dicionarioPalavras.append(Palavra("pessoa", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("casa", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("esperar", "verbo"))
dicionarioPalavras.append(Palavra("carteira", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("trabalho", "substantivo"))
dicionarioPalavras.append(Palavra("homem", "substantivo"))
dicionarioPalavras.append(Palavra("vizinho", "substantivo"))
dicionarioPalavras.append(Palavra("escola", "substantivo", "feminino"))

dicionarioExpressoes.append(["carteira trabalho",Expressoes("carteira de trabalho", "feminina")])
dicionarioExpressoes.append(["homem vizinh@",Palavra("vizinho", "substantivo")])
dicionarioExpressoes.append(["casa estudo",Palavra("escola", "substantivo", "feminino")])

def pesquisarPalavra(palavra):
    for item in dicionarioPalavras:
        if(palavra == item.sintaxe):
            return item
    
    return Palavra("","")

def ehSubstantivo(palavra):
    existe = pesquisarPalavra(palavra)
    if(existe.classificacao == "substantivo"):
        return True
    else:
        return False
    
def pesquisarExpressao(frase):
    expressoesAchadas = []
    bases = []

    for item in dicionarioExpressoes:
        if(item[0] in frase or item[1].sintaxe in frase):
            expressoesAchadas.append(item[1])
            bases.append(item[0])
    
    return expressoesAchadas, bases

def corrigirSubstantivo(frase):
    expressoes, bases = pesquisarExpressao(frase)
    return expressoes, bases