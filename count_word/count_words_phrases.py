import csv
from collections import Counter

# Palavras ou frases previamente selecionadas (substitua com suas palavras ou frases)
palavras = ['volunteered', 'volunteers', 'volunteer', 'geographic', 'information', 'quality', 'vgi', 'volunteer geographic information', 'volunteered geographic information', 'volunteered geographic', 'volunteer geographic', 'geographic information', 'quality of volunteered geographic information', 'vgi quality', 'quality of information', 'quality of vgi', 'quality assessment', 'data', 'openstreetmap', 'oms', 'spatial', 'mapping', 'map', 'analysis', 'urban', 'citizen', 'citizen', 'geospatial', 'framework', 'contributors', 'users', 'dataset', 'datasets', 'science', 'crowdsourced', 'crowdsourcing', 'spatial data quality' ,'spatial data', 'quality of spatial data']


# Inicializar contador de palavras
contador = Counter()

# Ler o arquivo de texto
with open('abstract.txt', 'r', encoding='utf-8') as arquivo_texto:
    texto_completo = arquivo_texto.read()

    # Processar cada palavra ou frase
    for palavra in palavras:
        # Atualizar a contagem para cada palavra ou frase
        contador[palavra] = texto_completo.lower().count(palavra.lower())

# Ordenar por frequência em ordem decrescente
contagem_ordenada = sorted(contador.items(), key=lambda x: x[1], reverse=True)

# Escrever no arquivo CSV
with open('phrases_frequencies.csv', 'w', newline='') as csv_saida:
    campo_nomes = ['weight', 'word']
    escritor_csv = csv.DictWriter(csv_saida, fieldnames=campo_nomes)

    escritor_csv.writeheader()
    for palavra, frequencia in contagem_ordenada:
        escritor_csv.writerow({'weight': frequencia, 'word': palavra})

print('Arquivo CSV gerado com sucesso!')