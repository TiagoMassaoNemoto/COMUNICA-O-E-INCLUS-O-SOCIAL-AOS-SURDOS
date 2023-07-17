from corrigirFrase import *
from  frasesCorrigidas import respostaPronta

#frases.append("hoje eu trabalhar muit@ eu precisar tempo")
#frases.append("m@ trabalho não ter carteira trabalho assinad@")
#frases.append("você b o l o fazer errad@")
#frases.append("família m@ surda")
#frases.append("documento ess@ ilegal")
#frases.append("homem vizinh@ legal sempre brincar pessoa tod@")
#frases.append("eu comprar casa nov@ agora esperar documento legalizar")
#frases.append("esperar pouc@ eu ir banco")
#frases.append("tod@ casa estudo normal aula começar fevereiro o u março")

palavras = []

def addPalavra(palavra):
    palavras.append(palavra)

    fraseCorrigida = identificarLetras(" ".join(palavras))
    fraseCorrigida, expressoesIdentificadas = checarExpressoes(fraseCorrigida)
    fraseCorrigida = corrigirGeneros(manterExpressoes(fraseCorrigida, expressoesIdentificadas))

    #print(fraseCorrigida)
    rp = respostaPronta(fraseCorrigida)

    if (rp != False):
        print(rp)
        palavras = []
    else:
        cf = corrigirFrase(fraseCorrigida)
        print(cf)
        palavras = []

addPalavra("cachorro")
addPalavra("est@")
addPalavra("b")
addPalavra("o")
addPalavra("m")
addPalavra("obediente")