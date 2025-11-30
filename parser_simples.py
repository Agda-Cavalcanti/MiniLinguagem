# Verifica se a sequência de tokens faz sentido de acordo com a gramática da linguagem.
from tabela_afn_afd import *

def leitura_dos_tokens(sentenca):

    estado_atual = estado_inicial

    for simbolo in sentenca:

        # Entrada de símbolo inválido
        if simbolo not in alfabeto:
            return False

        # Não há transição 
        if simbolo not in transicoes[estado_atual]:
            return False

        # Transição feita
        estado_atual = transicoes[estado_atual][simbolo]

    # Aceita se terminar destrancada
    return estado_atual in estado_final

