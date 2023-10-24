# Importando libs
from arcgis.gis import GIS
from shapely.geometry import Point, Polygon
from arcgis.features import FeatureLayer
import math, pyproj
from arcgis.features import FeatureLayer, use_proximity

# url
urlAgo = 'https://www.arcgis.com'
urlEnter = 'https://ide.unb.br/portal/'

# Acessando as plataformas
gisAgo = GIS(urlAgo, 'fortunatompongo_UnB', 'EuamoaKelly1994')
gisEnter = GIS(urlEnter, '210033525', 'EuamoaKelly1994')

# Get data UnB
# Ago content
limite_unb = gisAgo.content.get('0dc1a7598ca04fc5971440b8875ec6d4').layers[0]

# Ago group
myAgoGroup = gisAgo.groups.search('Projeto SmartCampus')
myAgoGroupId = myAgoGroup[0].id
myAgoGroupContent = gisAgo.groups.get(myAgoGroupId)

mylist = ['Árvores do Campus', 'Resíduos', 'Infraestrutura Esgoto', 'Infraestrutura Energia', 'Infraestrutura Água', 'Vias de Circulação', 'Segurança', 'Sanitários', 'Paradas Quickcapture']

selectlist = []

for item in mylist:
    for content in myAgoGroupContent.content():
        if item == content.title:
            print(item, len(content.layers[0].query().features))
            selectlist.append(content)

# Enter group
myEnterGroup = gisEnter.groups.search('Smart Campus - UnB (Dados Básicos)')
groupId = myEnterGroup[0].id
myEnterGroupContent = gisEnter.groups.get(groupId)

# Get camada
limit_features = limite_unb.query().features
# Get geometry da camada
limit_geometries = [feature.geometry for feature in limit_features]

limit_polygons = [Polygon(geom['rings'][0]) for geom in limit_geometries]

arvoreIsolada = []
for indice, arvore in enumerate(myEnterGroupContent.content()):
    print(indice, arvore)
    if arvore.title == 'Arvore_Isolada':
        print('Selecionado' , FeatureLayer(arvore))
        arvoreIsolada.append(arvore)

arvore_isolada = arvoreIsolada[0].layers[0]

# Get camada pontos
pontos = arvore_isolada.query().features

# print('pontos', pontos)

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

# print('dados')
# print(arvores_dentro[0].geometry)


# verificação de pontos fora e dentro do limite da UnB
origem_proj = pyproj.Proj(init='EPSG:102100')
destino_proj = pyproj.Proj(init='EPSG:31983')
pontos_dentro = []
pontos_fora = []

for content_group in selectlist:
    pontos_camada = content_group.layers[0].query().features

    for ponto in pontos_camada:
        if  ponto.geometry and 'x' in ponto.geometry:
            coordenada = ponto.geometry['x'], ponto.geometry['y']

            x_transformed, y_transformed = pyproj.transform(origem_proj, destino_proj, coordenada[0], coordenada[1])
            # coordenada = ponto.geometry['x'], ponto.geometry['y']
            coordenada_shapely = Point(x_transformed, y_transformed)

            dentro = False
            for polygon in limit_polygons:
                if coordenada_shapely.within(polygon):
                    dentro = True
                    break
            if dentro:
                pontos_dentro.append({ 'coordenada': coordenada_shapely, 'ponto': ponto, 'title': content_group.title })
            else:
                pontos_fora.append({ 'coordenada': coordenada_shapely, 'ponto': ponto, 'title': content_group.title })

print(f"Pontos dentro do limite: {len(pontos_dentro)}")
print(f"Pontos fora do limite: {len(pontos_fora)}")
print('pontos_fora', pontos_fora)


# pontos válidos para análise

raio = 5  # em metros

pontos_sobrepostos = []
mylist = ['Árvores do Campus', 'Resíduos', 'Infraestrutura Esgoto', 'Infraestrutura Energia', 'Infraestrutura Água', 'Vias de Circulação', 'Segurança', 'Sanitários', 'Paradas Quickcapture']

arvore_isolad = arvoreIsolada[0].layers
test = selectlist[0].layers[0]

# buffer_resultado = use_proximity.create_buffers(gisAgo, inputs=[ponto_origem], distances=[1000], units='Meters')

ports_buffer50 = use_proximity.create_buffers(test, distances=[5], units = 'Meters')

# camada_referencia = FeatureLayer(selectlist[0])

# # Camada do buffer
# camada_buffer = ports_buffer50.layers[0].url

# print(camada_buffer)


                                # criando buffer das camadas

buffer5_pontos_dentro = []

print('pontos_dentro', pontos_dentro[0])
print('dir', dir(pontos_dentro[0]))
print('pontos_', test)

for item in pontos_dentro:
    data = item['coordenada']
    point_buffer5 = use_proximity.create_buffers(data, distances=[5], units = 'Meters')
    buffer5_pontos_dentro.append({ 'type': point_buffer5, 'title': item.title })


print('buffer5_pontos_dentro', buffer5_pontos_dentro)

                                # feature buffer

points_look = []

for item in buffer5_pontos_dentro:

    feature_ports_buffer5 = item.layer.featureSet.features
    limit_feature_buffer5 = [feature.geometry for feature in feature_ports_buffer5]
    limit_polygons_buffer5 = [Polygon(geom['rings'][0]) for geom in limit_feature_buffer5]

    if item.title == 'Árvores do Campus':
        for i in limit_polygons_buffer5:
            for y in myEnterGroupContent.content()[0]:
                if i.contains(y):
                    points_look.append(y)


print(points_look)

# print('buffer5_list', buffer5_pontos_dentro[0])
# print('selectlist', selectlist)
# print('limit_features', limit_features)
# # print(dir(use_proximity))
# # print(help(use_proximity))
# # print('antes', ports_buffer50.layer.featureSet.features[2])
# feature_ports_buffer50 = ports_buffer50.layer.featureSet.features
# # print('antes', feature_ports_buffer50)
# print(dir(ports_buffer50.layer.featureSet.features[0]))
# # print(dir(use_proximity.create_buffers))

# # get all geometry
# limit_ports_buffer50 = [feature.geometry for feature in feature_ports_buffer50]

# # transform do polygon
# limit_polygons_ports_buffer50 = [Polygon(geom['rings'][0]) for geom in limit_ports_buffer50]

# print('limit_polygons_ports_buffer50', limit_polygons_ports_buffer50)






# for item in ports_buffer50:
#     camada_buffer = item['url']
#     # Faça algo com a camada_buffer, como imprimir
#     print(camada_buffer)

# Identificar os pontos que estão dentro do buffer
# resultado = use_proximity.find_existing_locations(camada_referencia, camada_buffer)

# for feature in resultado:
#     print(f"ID do ponto dentro do buffer: {feature.attributes['ID']}")


# for i, ponto1 in enumerate(pontos_dentro):
#     coordenada_ponto1 = ponto1['ponto'].geometry['x'], ponto1['ponto'].geometry['y']

#     ponto1_x_transformed, ponto1_y_transformed = pyproj.transform(origem_proj, destino_proj, coordenada_ponto1[0], coordenada_ponto1[1])
    
#     for normalizada in myEnterGroupContent.content():
#         # as camadas de quick capture têm que ter mesmo nome das normalizadas
#         # print(normalizada.title)

#         # Arvore_Isolada e Árvores do Campus
#         if normalizada.title == 'Arvore_Isolada' and ponto1['camada'] == mylist[0]:
#             camada_normalizada = normalizada.layers[0].query().features

#             for item_normalizado in camada_normalizada:
#                 print(i, item_normalizado)
#                 # print('ponto2', i, ponto2['camada'])
#                 # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
#                 # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

                

#                 if 'x' in item_normalizado.geometry:
#                     ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

#                     normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
#                     distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
#                     if distancia <= raio:
#                         pontos_sobrepostos.append(ponto1)
#                         break  # Para evitar verificações duplicadas
        
        # # Boca_Lobo e Infraestrutura Água
        # if normalizada.title == 'Boca_Lobo' and ponto1['camada'] == mylist[4]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Cameras e Segurança
        # if normalizada.title == 'Cameras' and ponto1['camada'] == mylist[6]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Centro_Edificacao e Centro das Edificacoes
        # if normalizada.title == 'Centro_Edificacao' and ponto1['camada'] == mylist[4]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Ciclovia e Vias de Circulação
        # if normalizada.title == 'Ciclovia' and ponto1['camada'] == mylist[5]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Conteiner e Resíduos
        # if normalizada.title == 'Conteiner' and ponto1['camada'] == mylist[1]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Edif_Ensino e Edificacoes
        # if normalizada.title == 'Edif_Ensino' and ponto1['camada'] == mylist[4]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Estacionamento e Estacionamentos
        # if normalizada.title == 'Estacionamento' and ponto1['camada'] == mylist[4]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Estrut_Apoio e Paradas Quickcapture
        # if normalizada.title == 'Estrut_Apoio' and ponto1['camada'] == mylist[8]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Galeria_Bueiro e Infraestrutura Água
        # if normalizada.title == 'Galeria_Bueiro' and ponto1['camada'] == mylist[4]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Passeio e Vias de Circulação
        # if normalizada.title == 'Passeio' and ponto1['camada'] == mylist[5]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Poste e Infraestrutura Energia
        # if normalizada.title == 'Poste' and ponto1['camada'] == mylist[3]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

        # # Trecho_Rodoviario e Vias de Circulação
        # if normalizada.title == 'Trecho_Rodoviario' and ponto1['camada'] == mylist[5]:
        #     camada_normalizada = normalizada.layers[0].query().features

        #     for item_normalizado in camada_normalizada:
        #         print(i, item_normalizado)
        #         # print('ponto2', i, ponto2['camada'])
        #         # if ponto1['ponto'].attributes['objectid'] and ponto2['ponto'].attributes['objectid']:
        #         # if ponto1['ponto'].attributes['objectid'] != ponto2['ponto'].attributes['objectid']:

        #         if 'x' in item_normalizado.geometry:
        #             ponto_normalizado = item_normalizado.geometry['x'], item_normalizado.geometry['y']

        #             normalizado_x_transformed, normalizado_y_transformed = pyproj.transform(origem_proj, destino_proj, ponto_normalizado[0], ponto_normalizado[1])
                    
        #             distancia = math.sqrt((ponto1_x_transformed - normalizado_x_transformed)**2 + (ponto1_y_transformed - normalizado_y_transformed)**2)
                    
        #             if distancia <= raio:
        #                 pontos_sobrepostos.append(ponto1)
        #                 break  # Para evitar verificações duplicadas

print(pontos_sobrepostos)
print(len(pontos_sobrepostos))