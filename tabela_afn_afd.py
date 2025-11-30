# Estados
estados = {"trancada", "destrancada"}

# Alfabeto
alfabeto = {"usar_chave", "reset"}

# Estado inicial
estado_inicial = "trancada"

# Estado final 
estado_final = {"destrancada"}

# Tabela de transições
transicoes = {
    "trancada": {
        "usar_chave": "destrancada"
    },
    "destrancada": {
        "reset": "trancada"
    }
}