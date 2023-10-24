# https://www.arcgis.com

# prmeiro instalar o conda:
    # wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    # bash miniconda.sh
    # conda --version

# criar o ambiente conda:
    # conda create --name agodata

# ativar o ambiente conda:
    # conda activate agodata

# importar a api para argis online
from arcgis.gis import GIS
# importando display
from IPython.display import display
# importando biblioteca para manipulação de camada de coleção de feições
from arcgis.features import FeatureLayerCollection as flc
# imporatando biblioteca para manipulação de camadas
from arcgis.features import FeatureLayer
#  importando pandas
import pandas as pd
# importando geometry - não funcionou e fiz o passo abaixo
from arcgis import geometry
# pip install shapely
from shapely.geometry import Point, Polygon

# para impedir que limite linhas e colunas
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)


urlAgo = 'https://www.arcgis.com'
urlEnter = 'https://ide.unb.br/portal/'
# https://ide.unb.br/portal/home/index.html
# https://ide.unb.br/

# acessando ago
gisAgo = GIS(urlAgo, 'fortunatompongo_UnB', 'EuamoaKelly1994')
gisEnter = GIS(urlEnter, '210033525', 'EuamoaKelly1994')

# vendo as propriedades do GIS
# print('GIS proprities', dir(gis))

meAgo = gisAgo.users.me
meEnter = gisEnter.users.me

portalAgo = gisAgo.properties.portalName
portalEnter = gisEnter.properties.portalName

print(meAgo,':', portalAgo, '.', meEnter, ':', portalEnter)

# grupos

# print('GIS proprities', dir(gisEnter))

myEnterGroup = gisEnter.groups.search('Smart Campus - UnB (Dados Básicos)')
groupId = myEnterGroup[0].id
myEnterGroupContent = gisEnter.groups.get(groupId)

# camada limite da UnB no AGO
print('camada limite da UnB no AGO')
limitAgoContent = gisAgo.content.get('9704885bbcaf486788c2ffb6ab602c97').layers[0].query().sdf['SHAPE']
# limit_unb_ago_content = gisAgo.content.get('9704885bbcaf486788c2ffb6ab602c97').layers[0]
limite_unb = gisAgo.content.get('0dc1a7598ca04fc5971440b8875ec6d4').layers[0]
# print(limitAgoContent.head())
# print(limitAgoContent['SHAPE'])
# print(limitAgoContent)
limitAgoGeometry = limite_unb.properties.extent.spatialReference

print('camada limite da UnB no AGO array')
arvoreIsolada = []
for indice, arvore in enumerate(myEnterGroupContent.content()):
    print(indice, arvore)
    if arvore.title == 'Arvore_Isolada':
        print('Selecionado' , FeatureLayer(arvore))
        arvoreIsolada.append(arvore)

# extensões da camada
print('extensões da camada')
analise = arvoreIsolada[0].layers[0].properties.extent
# print(analise)

# camada arvore isolada
print('camada arvore isolada')
arvore_isolada = arvoreIsolada[0].layers[0]
print(arvore_isolada)

# spatial reference
print('sistema_de_coordenadas_arvore')
sistema_de_coordenadas_arvore = arvore_isolada.properties.extent.spatialReference
sistema_de_coordenadas_limite = limite_unb.properties.extent.spatialReference
print(sistema_de_coordenadas_arvore)
print('sistema_de_coordenadas_limite')
print(sistema_de_coordenadas_limite)
# camada_arvore_isolada = 

# pontos = arvore_isolada.query().sdf['SHAPE']
pontos = arvore_isolada.query().features

# pontos = [Point(xy) for xy in zip(arvore_isolada.query().sdf['SHAPE'].apply(lambda geom: geom.x), arvore_isolada.query().sdf['SHAPE'].apply(lambda geom: geom.y))]
# limit_polygon = Polygon(limitAgoContent.geometry.iloc[0].rings[0])
# limit_polygon = Polygon(limitAgoContent.iloc[0].SHAPE)
# limit_polygon = geometry(limit_unb_ago_content)

print('limit_features')
limit_features = limite_unb.query().features
# print(limit_features)
print('limit_geometries')
limit_geometries = [feature.geometry for feature in limit_features]
# print(limit_geometries)

# if ponto.within(limitAgoContent):
# excluindo quem está fora
print('excluindo quem está fora')
# for ponto in pontos:
#     if ponto.within(limit_polygon):
#         print("Ponto está dentro do polígono")
#     else:
#         print("Ponto não está dentro de nenhum polígono")

# for ponto in pontos:
#     point_inside = False
#     for polygon in limit_polygon:
#         if ponto.within(polygon):
#             point_inside = True
#             break
#     if point_inside:
#         print("Ponto está dentro do polígono")
#     else:
#         print("Ponto não está dentro de nenhum polígono")

# for ponto in pontos:
#     if ponto.within(limit_geometries):
#         print("Ponto está dentro do polígono")
#     else:
#         print("Ponto não está dentro de nenhum polígono")
# arvore_isolada_unb = []
# arvore_isolada_fora = []

limit_polygons = [Polygon(geom['rings'][0]) for geom in limit_geometries]

arvores_dentro = []
arvores_fora = []

for feature in pontos:
    ponto = feature.geometry['x'], feature.geometry['y']
    ponto_shapely = Point(ponto[0], ponto[1])
    
    dentro = False
    for polygon in limit_polygons:
        if ponto_shapely.within(polygon):
            dentro = True
            break
    if dentro:
        arvores_dentro.append(feature)
    else:
        arvores_fora.append(feature)

print(f"Árvores dentro do limite: {len(arvores_dentro)}")
print(f"Árvores fora do limite: {len(arvores_fora)}")

print('dados')
print(arvores_dentro[0].geometry)

layer_properties = {
    "title": "Camada de Árvores Fora",
    "tags": "arvores, fora",
    "type": "Feature Layer",
    "overwrite": True 
}
arvores_layer = gisAgo.content.add(item_properties=layer_properties)

# Carregando os dados
arvores_layer.edit_features(adds=arvores_dentro)

# filtro usando geometry
# for ponto in camada_arvore_isolada:
#     if geometry.contains(limitAgoContent, ponto):
#         arvore_isolada_unb.append(ponto)
#     else:
#         arvore_isolada_fora.append(ponto)

# for ponto in camada_arvore_isolada:
#     if limitAgoContent.contains(ponto):
#         arvore_isolada_unb.append(ponto)
#     else:
#         arvore_isolada_fora.append(ponto)

# print('arvore_isolada_unb', len(arvore_isolada_unb))
# print('arvore_isolada_fora', len(arvore_isolada_fora))

# # tabela de atributos
# tabelaAtributosarvore = arvore_isolada.query().sdf
# print(tabelaAtributosarvore)


# arvoreIsolada = []
# print(type(myGroupContent))
# for indice, arvore in enumerate(myGroupContent):
#     print(f"Índice: {indice}, Tipo: {type(arvore)}, Conteúdo: {arvore}")
#     print(f"Título: {arvore.title if hasattr(arvore, 'title') else 'Atributo não encontrado'}")
#     if hasattr(arvore, 'title') and isinstance(arvore.title, str) and arvore.title.strip() == 'Arvore_Isolada':
#         print(f"Árvore Isolada encontrada: {arvore}")
#         arvoreIsolada.append(arvore)

# print(arvoreIsolada)

# print('myEnterGroup proprities', dir(myEnterGroup))
# 149d525db80d41598004241e94ac648b - Smart Campus
# print(len(myEnterGroup))

# print('Conteudo', myGroupContent.content()[0].owner)


my_content = gisAgo.content.search('BaseMapFieldMap')
# print(my_content)

my_content_by_id = gisAgo.content.get('496569314a05446a8672848c3278bb0f')
# print(type(my_content_by_id.type))

all_content = gisAgo.content.search(query="", max_items=1000)
# print(all_content)

# for item in all_content:
#     if item.type != 'Feature Layer Collection':
#         print('lista', type(item))

collectionsLayer = FeatureLayer(my_content_by_id)
# print(collectionsLayer)



# removido main:

pontos_dentro = []
pontos_fora = []

for content_group in myEnterGroupContent.content():
    pontos_camada = content_group.layers[0].query().features

    for ponto in pontos_camada:
        if  ponto.geometry and 'x' in ponto.geometry:
            coordenada = ponto.geometry['x'], ponto.geometry['y']
            coordenada_shapely = Point(coordenada[0], coordenada[1])

            dentro = False
            for polygon in limit_polygons:
                if coordenada_shapely.within(polygon):
                    dentro = True
                    break
            if dentro:
                pontos_dentro.append({ 'ponto': ponto, 'camada': content_group.title })
            else:
                pontos_fora.append({ 'ponto': ponto, 'camada': content_group.title })

print(f"Pontos dentro do limite: {len(pontos_dentro)}")
print(f"Pontos fora do limite: {len(pontos_fora)}")

# pontos válidos para análise

raio = 5  # em metros

pontos_sobrepostos = []

for i, ponto1 in enumerate(pontos_dentro):
    coordenada_ponto1 = ponto1['ponto'].geometry['x'], ponto1['ponto'].geometry['y']

    ponto1_x_transformed, ponto1_y_transformed = pyproj.transform(origem_proj, destino_proj, coordenada_ponto1[0], coordenada_ponto1[1])
    
    for ponto2 in pontos_dentro[i+1:]:
        print('ponto2', i, ponto2['camada'])
        # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        coordenada_ponto2 = ponto2['ponto'].geometry['x'], ponto2['ponto'].geometry['y']

        ponto2_x_transformed, ponto2_y_transformed = pyproj.transform(origem_proj, destino_proj, coordenada_ponto2[0], coordenada_ponto2[1])
        
        distancia = math.sqrt((ponto1_x_transformed - ponto2_x_transformed)**2 + (ponto1_y_transformed - ponto2_y_transformed)**2)
        
        if distancia <= raio:
            pontos_sobrepostos.append(ponto1)
            break  # Para evitar verificações duplicadas

print(pontos_sobrepostos)
print(len(pontos_sobrepostos))