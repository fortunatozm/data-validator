import csv
from collections import Counter
import string

# Palavras previamente selecionadas (substitua com suas palavras)
palavras = ['volunteered', 'volunteer', 'geographic', 'information', 'vgi', 'volunteer geographic information', 'quality assessment' ]

# Inicializar contador de palavras
contador = Counter()

# Ler o arquivo de texto
with open('abstract.txt', 'r', encoding='utf-8') as arquivo_texto:
    for linha in arquivo_texto:
        # Processar cada palavra na linha
        palavras_no_texto = linha.lower().split()  # Converte para minúsculas
        palavras_no_texto = [palavra.strip(string.punctuation) for palavra in palavras_no_texto]

        # Atualizar a contagem para cada palavra
        for palavra in palavras_no_texto:
            if palavra in palavras:
                contador[palavra] += 1

# Escrever no arquivo CSV
with open('words_frequencies.csv', 'w', newline='') as csv_saida:
    campo_nomes = ['Weight', 'Words']
    escritor_csv = csv.DictWriter(csv_saida, fieldnames=campo_nomes)

    escritor_csv.writeheader()
    for palavra, frequencia in contador.items():
        escritor_csv.writerow({'Weight': frequencia, 'Words': palavra})

print('Arquivo CSV gerado com sucesso!')




