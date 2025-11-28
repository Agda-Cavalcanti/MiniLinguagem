from parser_simples import reconhecer_sentenca
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
        resultado = "ACEITO" if reconhecer_sentenca(linha) else "REJEITADO"
        linha_formatada = linha.strip()
        print(f"{linha_formatada} => {resultado}")
        log.write(f"{linha_formatada} => {resultado}\n")