frasesCorrigidas = []

def addFrase(fraseInicio, fraseCorrigida):
    frasesCorrigidas.append([len(fraseInicio.split()), fraseInicio, fraseCorrigida])

def respostaPronta(fraseInicio):
    for frase in frasesCorrigidas:
        if(len(fraseInicio) == frase[0]):
            if(fraseInicio == frase[1]):
                return frase[2]
    
    return False