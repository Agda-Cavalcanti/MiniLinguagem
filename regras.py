from tabela_afn_afd import tokens_validos, linguagem_utilizada
print("Tokens disponíveis na linguagem:")
for token in tokens_validos:
    print(f"- {token}")
print("\nSequências válidas da linguagem:")
for regra in linguagem_utilizada:
    print(" ".join(regra))