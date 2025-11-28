# Verifica se a sequência de tokens faz sentido de acordo com a gramática da linguagem.
from tabela_afn_afd import linguagem_utilizada
def reconhecer_sentenca(sentenca):
    palavras = sentenca.strip().split()
    for regra in linguagem_utilizada:
        if palavras == regra:
            return True
    return False