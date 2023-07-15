from palavrasClasse import *

def juntarLetras(letras):
    palavra = ""
    palavrasCorrigidas = []

    for letra in letras:
        if(letra != "-"):
            palavra += letra
        else:
            palavrasCorrigidas.append(palavra)
            palavra = ""
    
    return palavrasCorrigidas

def definirGenero(palavra, referencia):
    if(referencia.classificacao == "verbo"):
        return definirMasculino(palavra)
    elif(referencia.classificacao == "substantivo"):
        if(referencia.genero == "masculino"):
            return definirMasculino(palavra)
        else:
            return definirFeminino(palavra)
    else:
        if(referencia.genero == "masculino"):
            return definirMasculino(palavra)
        else:
            return definirFeminino(palavra)

def definirMasculino(palavra):
    if(palavra == "m@"):
        return palavra.replace("@", "eu")
    elif(palavra == "est@" or palavra == "ess@"):
        return palavra.replace("@", "e")
    else:
        return palavra.replace("@", "o")

def definirFeminino(palavra):
    if(palavra == "m@"):
        return palavra.replace("@", "inha")
    else:
        return palavra.replace("@", "a")
