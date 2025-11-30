from parser_simples import leitura_dos_tokens
import datetime

entrada = "testes.txt"
saida = "log_saida.txt"

with open(entrada,'r') as f:
    sentencas = f.readlines()
# Log da execução
with open(saida,'w') as log:
    log.write("===== Log de Execução da Mini Linguagem =====\n")
    log.write(f"Data: {datetime.datetime.now()}\n\n")
    log.write("Sentenças analisadas:\n")
    
    for linha in sentencas:
        tokens = linha.strip().split()

        resultado = "ACEITO" if leitura_dos_tokens(tokens) else "REJEITADO"

        print(f"{linha.strip()} => {resultado}")
        log.write(f"{linha.strip()} => {resultado}\n")