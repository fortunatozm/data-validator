import matplotlib.pyplot as plt

label1 = ['Postes', 'Estacionamentos', 'Coletores de lixo', 'Conteiner de residuos', 'Coletores para reciclagem', 'Bueiros', 'Bocas de lobo', 'Refletores', 'Água amarrações', 'Escultura']
label2 = ['Refletores', 'Água amarrações', 'Escultura']
label3 = ['Parada de onibus', 'Bacia PE', 'Containers de Sala', 'Subestacões de energia', 'Pontos de segurança', 'Torres de transmissão', 'Árvores', 'Edificações', 'Energia iluminação pública', 'Esgoto componentes', 'nones']

label_points1 = [606, 261, 98, 68, 50, 45, 26, 22, 20, 17]
label_points2 = [22, 20, 17]
label_points3 = [15, 14, 13, 12, 5, 5, 3, 2, 2, 1, 38]

#  'pontos_seguranca', 'torredetransmissao', 'arvores', 'edificacoes', 'energia_iluminacao_publica', 'esgoto_componentes',

#  5, 5, 3, 2, 2, 1, 

fig, ax = plt.subplots(figsize=(14,14))

# def func(pct, allvalues):
#     absolute = int(pct / 100. * sum(allvalues))
#     return f"{pct:.1f}%\n({absolute})"

# explode = [0.05] * len(label2)

# Criar o gráfico de pizza
wedges, texts, autotexts = ax.pie(label_points1, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))

for autotext in autotexts:
    autotext.set_fontsize(12)
# Ajustar o tamanho dos textos dos rótulos e dos percentuais
# for text in texts:
#     text.set_fontsize(10)
# for autotext in autotexts:
#     autotext.set_fontsize(10)

# explode = [0.05] * len(label)

# explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# ax.pie(label_points, autopct='%.1f%%', startangle=60)
ax.set_title('Quantidade de coleta por camada', fontsize=16)

plt.legend(label1 ,loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()