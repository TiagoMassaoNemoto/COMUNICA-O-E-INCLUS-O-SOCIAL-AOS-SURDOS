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
dicionarioPalavras.append(Palavra("mulher", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("vizinho", "substantivo"))
dicionarioPalavras.append(Palavra("vizinha", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("escola", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("saudade", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("dor", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("doença", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("saúde", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("febre", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("gostar", "verbo"))
dicionarioPalavras.append(Palavra("estudar", "verbo"))
dicionarioPalavras.append(Palavra("ter", "verbo"))
dicionarioPalavras.append(Palavra("dia", "substantivo"))
dicionarioPalavras.append(Palavra("mês", "substantivo"))
dicionarioPalavras.append(Palavra("semana", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("ajudar", "verbo"))
dicionarioPalavras.append(Palavra("parar", "verbo"))
dicionarioPalavras.append(Palavra("esperar", "verbo"))
dicionarioPalavras.append(Palavra("demorar", "verbo"))
dicionarioPalavras.append(Palavra("comer", "verbo"))
dicionarioPalavras.append(Palavra("comprar", "verbo"))
dicionarioPalavras.append(Palavra("pagar", "verbo"))
dicionarioPalavras.append(Palavra("saber", "verbo"))
dicionarioPalavras.append(Palavra("entender", "verbo"))
dicionarioPalavras.append(Palavra("nascer", "verbo"))
dicionarioPalavras.append(Palavra("morrer", "verbo"))
dicionarioPalavras.append(Palavra("bonito", "adjetivo"))
dicionarioPalavras.append(Palavra("bonita", "adjetivo", "feminino"))
dicionarioPalavras.append(Palavra("feio", "adjetivo"))
dicionarioPalavras.append(Palavra("feia", "adjetivo", "feminino"))
dicionarioPalavras.append(Palavra("magro", "adjetivo"))
dicionarioPalavras.append(Palavra("magra", "adjetivo", "feminino"))
dicionarioPalavras.append(Palavra("gordo", "adjetivo"))
dicionarioPalavras.append(Palavra("gorda", "adjetivo", "feminino"))
dicionarioPalavras.append(Palavra("educado", "adjetivo"))
dicionarioPalavras.append(Palavra("educada", "adjetivo", "feminino"))
dicionarioPalavras.append(Palavra("rápido", "adjetivo"))
dicionarioPalavras.append(Palavra("rápida", "adjetivo", "feminino"))
dicionarioPalavras.append(Palavra("inteligente", "adjetivo"))
dicionarioPalavras.append(Palavra("gratuito", "adjetivo"))
dicionarioPalavras.append(Palavra("quente", "adjetivo"))
dicionarioPalavras.append(Palavra("legal", "adjetivo"))
dicionarioPalavras.append(Palavra("vídeo", "substantivo"))
dicionarioPalavras.append(Palavra("sinal", "substantivo"))
dicionarioPalavras.append(Palavra("amor", "substantivo"))
dicionarioPalavras.append(Palavra("dinheiro", "substantivo"))
dicionarioPalavras.append(Palavra("polícia", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("bandido", "substantivo"))
dicionarioPalavras.append(Palavra("bandida", "substantivo", "feminino"))
dicionarioPalavras.append(Palavra("perigo", "substantivo"))
dicionarioPalavras.append(Palavra("segurança", "substantivo"))
dicionarioPalavras.append(Palavra("costume", "substantivo"))
dicionarioPalavras.append(Palavra("branco", "substantivo"))
dicionarioPalavras.append(Palavra("cruz", "substantivo"))

dicionarioExpressoes.append(["carteira trabalho",Expressoes("carteira de trabalho", "feminina")])
dicionarioExpressoes.append(["homem vizinh@",Palavra("vizinho", "substantivo")])
dicionarioExpressoes.append(["casa estudar",Palavra("escola", "substantivo", "feminino")])
dicionarioExpressoes.append(["casa cruz",Palavra("hospital", "substantivo")])

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