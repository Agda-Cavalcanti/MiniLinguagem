# Define quais tokens (palavras) existem na linguagem
tokens = {
"MOVE": "Verbo de ação",
"N": "Direção norte",
"S": "Direção sul",
"OPEN": "Ação de abrir",
"DOOR": "Objeto porta",
"PUSH": "Ação de empurrar",
"LEVER": "Objeto alavanca",
"EXIT": "Saída do jogo (AFN)"
}
# Define as sequências válidas (regras de produção)
linguagem_utilizada = [
["MOVE","N"],
["MOVE","S"],
["OPEN","DOOR"],
["PUSH","LEVER"],
["EXIT"]
]