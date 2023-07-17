from correcaoPalavras import definirGenero, juntarLetras
from palavrasClasse import *
from frasesCorrigidas import addFrase

def corrigirGeneros(palavras):
    for i in range(len(palavras)):
        if("@" in palavras[i]):
            if(i == 0):
                if(" " in palavras[i + 1]):
                    referencia = pesquisarExpressao(palavras[i + 1])
                    if(referencia):
                        palavras[i] = definirGenero(palavras[i],referencia)
                else:
                    referencia = pesquisarPalavra(palavras[i + 1])
                    if(referencia):
                        palavras[i] = definirGenero(palavras[i], referencia)
            else:
                if(" " in palavras[i - 1]):
                    referencia, base = pesquisarExpressao(palavras[i - 1])
                    if(referencia):
                        palavras[i] = definirGenero(palavras[i],referencia[0])
                else:
                    referencia = pesquisarPalavra(palavras[i - 1])
                    if(referencia):
                        palavras[i] = definirGenero(palavras[i], referencia)
    
    return " ".join(palavras)

def identificarExpressoes(frase):
    expressoesIdentificadas = []
    expressoesIdentificadasBase = []
    
    expressoes, bases = corrigirSubstantivo(frase)

    for i in range(len(expressoes)):
        expressoesIdentificadas.append(expressoes[i])
        expressoesIdentificadasBase.append(bases[i])

    return expressoesIdentificadas, expressoesIdentificadasBase

def manterExpressoes(frase, expressoes):
    palavras = []
    lista = []
    for i in range(len(expressoes)):
        frase = frase.replace(expressoes[i].sintaxe, str(i))
    
    palavras = frase.split()

    for palavra in palavras:
        ehNumero = isinstance(palavra, int)
        if(len(palavra) != 1 or ehNumero == False):
            lista.append(palavra)
        else:
            lista.append(expressoes[int(palavra)].sintaxe)

    return lista

def identificarLetras(frase):
    letras = []
    palavras = frase.split()
    fraseCorrigida = frase

    for i in range(len(palavras)):
        if(len(palavras[i]) == 1):
            letras.append(palavras[i])
        elif(i != 0 and len(palavras[i - 1]) == 1):
            letras.append("-")

    if(len(letras) > 0):
        palavrasCorrigidas = juntarLetras(letras)

        for palavra in palavrasCorrigidas:
            fraseCorrigida = fraseCorrigida.replace(" ".join(list(palavra)), palavra)
    
    return fraseCorrigida

def checarExpressoes(frase):
    expressoesIdentificadas = []
    expressoesIdentificadas, base = identificarExpressoes(frase)
    fraseCorrigida = frase

    if(len(expressoesIdentificadas) > 0):
        for i in range(len(expressoesIdentificadas)):
            if(expressoesIdentificadas[i]):
                fraseCorrigida = fraseCorrigida.replace(base[i], expressoesIdentificadas[i].sintaxe)

    return fraseCorrigida, expressoesIdentificadas

def corrigirFrase(frase):
    fraseFinal = frase
    
    tempo = identificarQuando(fraseFinal)

    #To do: Definir sujeito e predicado
    #To do: Identificar plural
    
    fraseFinal = correcao(tempo, cenario, objeto, sujeito, verbo, fraseFinal)
    
    addFrase(frase, fraseFinal)

    return fraseFinal

def identificarQuando(frase):
    if("amanhã" in frase):
        return "futuro"
    elif("ontem" in frase):
        return "passado"
    else:
        return "presente"
    
def correcao(tempo, cenario, objeto, sujeito, verbo, frase):
    #To do: Add artigos e preposiçoes
    
    #A lógica será melhor elaborada ainda

    if(tempo == "passado"):
        return frase.replace(verbo, conjugarVerbo(verbo, tempo))
    elif(tempo == "futuro"):
        return frase.replace(verbo, conjugarVerbo(verbo, tempo))
    else:
        return frase.replace(verbo, conjugarVerbo(verbo, tempo))