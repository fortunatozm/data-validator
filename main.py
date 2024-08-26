# Importando libs

print('teste')

import tempfile
import os
import io
import json
from arcgis.gis import GIS
from shapely.geometry import Point, Polygon
import csv
from arcgis.features import FeatureLayer, FeatureSet
from arcgis.features.feature import Feature
import math, pyproj
from arcgis.features import FeatureLayer, use_proximity
from arcgis.mapping import WebMap
from connection.conn_ago import connection_ago
from connection.conn_enterprise import connection_enter
from convert.jsontogeojson import convert_json_geojson
import geopandas as gpd


# Acessando as plataformas
print('Antes de logar')
gisAgo = connection_ago('fortunatompongo_UnB', 'EuamoaKelly1994')
# gisEnter = connection_enter('210033525', 'EuamoaKelly1994')

print('Depois de logar', gisAgo)

# Get data UnB
# Ago content
limite_unb_oficial = gisAgo.content.get('0dc1a7598ca04fc5971440b8875ec6d4').layers[0]
limite_unb = gisAgo.content.get('0dc1a7598ca04fc5971440b8875ec6d4').layers[0]
base_field_map = gisAgo.content.get('a75dd851c6d5436cb01a0ceaaa2a9013')

# print(len(base_field_map.layers[0].query().features))
# print('Field Map', poste.layers[0].query().features[0])

all_postes = []
tipo_coleta = []
all_arvores = []
all_camera = []
all_pontos_seguranca = []
all_coletoresparareciclagem = []
all_drenagem_bueiros = []
all_drenagem_bocas_lobo = []
all_caixasdeagua = []
all_energia_iluminacao_publica = []
all_esgoto_componentes = []
all_drenagem_bacia_pe = []
all_refletores = []
all_containersdesala = []
all_escultura = []
all_subestacoesdeenergias = []
all_parada_onibus = []
all_conteiner_residuos = []
all_agua_amarracoes = []
all_torredetransmissao = []
all_estacionamentos = []
all_edificacoes = []
all_coletoresd_lixo = []
all_nones = []

for data_base in base_field_map.layers[0].query().features:
    tipo_coleta.append(data_base.attributes['tipo_coleta'])

    data = data_base.attributes['tipo_coleta']

    #  or data == 'postes'
    if data == 'postes':
        all_postes.append(data_base)

    if data == 'arvore' or data == 'arvores':
        all_arvores.append(data_base)
        
    if data == 'pontos_seguranca':
        all_pontos_seguranca.append(data_base)

    if data == 'coletoresparareciclagem':
        all_coletoresparareciclagem.append(data_base)

    if data == 'drenagem_bueiros':
        all_drenagem_bueiros.append(data_base)

    if data == 'drenagem_bocas_lobo':
        all_drenagem_bocas_lobo.append(data_base)

    if data == 'caixasdeagua':
        all_drenagem_bocas_lobo.append(data_base)

    if data == 'energia_iluminacao_publica':
        all_energia_iluminacao_publica.append(data_base)

    if data == 'esgoto_componentes':
        all_esgoto_componentes.append(data_base)

    if data == 'drenagem_bacia_pe':
        all_drenagem_bacia_pe.append(data_base)

    if data == 'refletores':
        all_refletores.append(data_base)

    if data == 'containersdesala':
        all_containersdesala.append(data_base)

    if data == 'escultura':
        all_escultura.append(data_base)

    if data == 'subestacoesdeenergias':
        all_subestacoesdeenergias.append(data_base)

    if data == 'parada_onibus':
        all_parada_onibus.append(data_base)

    if data == 'conteiner_residuos':
        all_conteiner_residuos.append(data_base)

    if data == 'agua_amarracoes':
        all_agua_amarracoes.append(data_base)

    if data == 'torredetransmissao':
        all_torredetransmissao.append(data_base)

    if data == 'estacionamentos':
        all_estacionamentos.append(data_base)

    if data == 'edificacoes':
        all_edificacoes.append(data_base)

    if data == 'coletoresd lixo':
        all_coletoresd_lixo.append(data_base)

    if data == None:
        all_nones.append(data_base)

new_list = list(set(tipo_coleta))

print('new_list', new_list)

print('postes', len(all_postes))
print('arvores', len(all_arvores))
print('pontos_seguranca', len(all_pontos_seguranca))
print('coletoresparareciclagem', len(all_coletoresparareciclagem))
print('drenagem_bueiros', len(all_drenagem_bueiros))
print('drenagem_bocas_lobo', len(all_drenagem_bocas_lobo))
print('caixasdeagua', len(all_caixasdeagua))
print('energia_iluminacao_publica', len(all_energia_iluminacao_publica))
print('esgoto_componentes', len(all_esgoto_componentes))
print('drenagem_bacia_pe', len(all_drenagem_bacia_pe))
print('refletores', len(all_refletores))
print('containersdesala', len(all_containersdesala))
print('escultura', len(all_escultura))
print('subestacoesdeenergias', len(all_subestacoesdeenergias))
print('parada_onibus', len(all_parada_onibus))
print('conteiner_residuos', len(all_conteiner_residuos))
print('agua_amarracoes', len(all_agua_amarracoes))
print('torredetransmissao', len(all_torredetransmissao))
print('estacionamentos', len(all_estacionamentos))
print('edificacoes', len(all_edificacoes))
print('coletoresd_lixo', len(all_coletoresd_lixo))
print('nones', len(all_nones))

# verficar os que estão dentro do limite e fora

print('postes', all_postes[0])
# print('postes', all_postes)
print('type', type(all_postes))



poste_name = 'all_postes'

convert_json_geojson(poste_name, all_postes)

file_publish = 'all_postes.geojson'
print('file_publish', file_publish)

# with open(file_publish, 'r') as file:
#     geojson_data = file.read()

# with open('pontos.csv', 'r') as file:
#     arquivo_csv = io.StringIO(file.read())


# Leitura do arquivo GeoJSON
gdf = gpd.read_file(file_publish)


crs = 'EPSG:3857'

# Salvar como Shapefile
gdf.to_file('SHP/all_postes', driver='ESRI Shapefile', crs=crs)

# shp_publish = 'dados/dados.shp'

# Leitura do shapefile usando geopandas
# gdf_shp = gpd.read_file(shp_publish)

# Convertendo para GeoJSON
# geojson_data = gdf_shp.to_json()

# r'Caminho/para/o/seu/shapefile'

# Verifica se o item já existe
existing_poste_name = gisAgo.content.search(query=f"title:{poste_name}")

print('poste_name', existing_poste_name)

poste_properties = {
    "title": "Postes",
    "tags": "pontos, GIS, geojson, postes",
    "type": "GeoJson",
}

if existing_poste_name:
    for existing_item in existing_poste_name:
        if existing_item.owner == 'fortunatompongo_UnB':
            existing_item.delete()
    print(f"Item '{poste_name}' deletado com sucesso.")

    # Se o item não existe, crie-o
    # item_properties=poste_properties
# csv_poste = gisAgo.content.add(item_properties=poste_properties, data=geojson_data)

# params={"type":"geojson","locationType":"none"}

# try:
    # publish_parameters=params
    # csv_poste.publish()
# except Exception as e:
#     print(f"Erro durante a publicação do item: {str(e)}")


print('chegou aqui')


base_field_in = []
base_field_out = []

for feature in base_field_map.layers[0].query().features:
    ponto = feature.geometry['x'], feature.geometry['y']
    ponto_shapely = Point(ponto[0], ponto[1])
    
    dentro = False

    if ponto_shapely.within(limite_unb):
        dentro = True
        break
            
    if dentro:
        base_field_in.append(feature)
    else:
        base_field_out.append(feature)

print('base_field_in', len(base_field_in))
print('base_field_out', len(base_field_out))

# verificar a presença de atributos

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
limit_features = limite_unb_oficial.query().features
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
destino_proj_geo = pyproj.Proj(init='EPSG:4674')

pontos_dentro = []
pontos_fora = []

for content_group in selectlist:
    pontos_camada = content_group.layers[0].query().features

    for ponto in pontos_camada:
        if  ponto.geometry and 'x' in ponto.geometry:
            coordenada = ponto.geometry['x'], ponto.geometry['y']

            x_transformed, y_transformed = pyproj.transform(origem_proj, destino_proj, coordenada[0], coordenada[1])
            x_transformed_geo, y_transformed_geo = pyproj.transform(origem_proj, destino_proj_geo, coordenada[0], coordenada[1])
            # coordenada = ponto.geometry['x'], ponto.geometry['y']
            coordenada_shapely = Point(x_transformed, y_transformed)

            dentro = False
            for polygon in limit_polygons:
                if coordenada_shapely.within(polygon):
                    dentro = True
                    break
            if dentro:
                pontos_dentro.append({ 'coordenada23S': {'x': x_transformed, 'y': y_transformed}, 'ponto': ponto, 'title': content_group.title, 'coordenadageo': {'x': x_transformed_geo, 'y': y_transformed_geo} })
            else:
                pontos_fora.append({ 'coordenada23S': {'x': x_transformed, 'y': y_transformed}, 'ponto': ponto, 'title': content_group.title, 'coordenadageo': {'x': x_transformed_geo, 'y': y_transformed_geo} })

print(f"Pontos dentro do limite: {len(pontos_dentro)}")
print(f"Pontos fora do limite: {len(pontos_fora)}")
# print('pontos_fora', pontos_fora)


# pontos válidos para análise

raio = 5  # em metros

pontos_sobrepostos = []
mylist = ['Árvores do Campus', 'Resíduos', 'Infraestrutura Esgoto', 'Infraestrutura Energia', 'Infraestrutura Água', 'Vias de Circulação', 'Segurança', 'Sanitários', 'Paradas Quickcapture']

arvore_isolad = arvoreIsolada[0].layers
test = selectlist[0].layers[0]

# buffer_resultado = use_proximity.create_buffers(gisAgo, inputs=[ponto_origem], distances=[1000], units='Meters')

# ports_buffer50 = use_proximity.create_buffers(test, distances=[5], units = 'Meters')

# camada_referencia = FeatureLayer(selectlist[0])

# # Camada do buffer
# camada_buffer = ports_buffer50.layers[0].url

# print(camada_buffer)


                                # criando buffer das camadas

buffer5_pontos_dentro = []

print('pontos_dentro', len(pontos_dentro), pontos_dentro[0])
print('dir', dir(pontos_dentro[0]))
print('pontos_', test)


                                # criar camada de pontos dentro (apenas lista não manipulável)

pontos_dentro_lista_camada = []
for coord in pontos_dentro:

    if 'Problema' in coord['ponto'].attributes:
        ponto = {
            'geometry': {
                'x': coord['coordenada23S']['x'],
                'y': coord['coordenada23S']['y'],
                'spatialReference': {'wkid': 31983}
            },
            'attributes': {
                'OBJECTID': coord['ponto'].attributes['OBJECTID'],
                'Problema': coord['ponto'].attributes['Problema'],
                'Camada': coord['title']}
        }
        pontos_dentro_lista_camada.append(ponto)

camada_pontos_para_buffer = FeatureSet.from_dict(pontos_dentro_lista_camada)

print('camada_pontos_para_buffer', camada_pontos_para_buffer)
# print('pontos_dentro_lista_camada', pontos_dentro_lista_camada)
# temp_dir = tempfile.gettempdir()
# temp_path = os.path.join(temp_dir, "camada_temporaria")
# # Criar um arquivo temporário
# # temp_path = tempfile.mktemp(suffix=".json")

# # # Salvar FeatureSet no arquivo temporário
# # camada_pontos_para_buffer.save(temp_path, out_name="Camada_pre_buffer")

# features = []
# for coordenada in pontos_dentro:
#     ponto = {"x": coordenada['coordenada']['x'], "y": coordenada['coordenada']['y']}
#     feature = Feature(geometry=ponto)
#     features.append(feature)

# feature_set = FeatureSet(features)

# # Adicionar a camada de feições ao ArcGIS Online
# item_properties = {
#     "title": "Camada_pre_buffer",
#     "tags": "GIS, Camada, Buffer",
#     "type": "Feature Service",
#     "typeKeywords": "Data, Feature Service, Singlelayer",
#     "description": "Uma descrição opcional para a camada."
# }

# # Adicionar a camada de feições como um item ao ArcGIS Online
# feature_layer_item = gisAgo.content.add(item_properties=item_properties)

# # Publicar a camada de feições
# feature_layer = feature_layer_item.publish(overwrite=True, file_type='feature')

# print('Camada publicada:', feature_layer)


# Lista de dicionários com coordenadas x e y
coordenadas_pontos = [{'x': 10, 'y': 20}, {'x': 30, 'y': 40}, {'x': 50, 'y': 60}]

features = [{"geometry": {"x": item['x'], "y": item['y']}} for item in coordenadas_pontos]

print('pontos_dentro', pontos_dentro[0])

dados_pontos_analise = []

# estruturando dados dentro
for data in pontos_dentro:
    if 'Problema' in data['ponto'].attributes:
        dados_pontos_analise.append({
            "Latitude": data['coordenadageo']['y'],
            "Longitude": data['coordenadageo']['x'],
            "Nome": data['title'],
            "Problema": data['ponto'].attributes['Problema'],
            "Situação": "Ponto aprovado"
        })
    else:
        print('dados dentro que não foram estruturados', data)

# estruturando dados fora
for data in pontos_fora:
    if 'Problema' in data['ponto'].attributes:
        dados_pontos_analise.append({
            "Latitude": data['coordenadageo']['y'],
            "Longitude": data['coordenadageo']['x'],
            "Nome": data['title'],
            "Problema": data['ponto'].attributes['Problema'],
            "Situação": "Ponto rejeitado"
        })
    else:
        print('dados fora que não foram estruturados', data)

print('dados_pontos_dentro', dados_pontos_analise[0])

# Nome do arquivo CSV
nome_arquivo = "pontos.csv"

# Escrever no arquivo CSV
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    # Cria o escritor CSV
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=["Nome", "Problema", "Situação", "Longitude", "Latitude"])
    # Escreve o cabeçalho
    escritor_csv.writeheader()
    # Escreve os dados
    escritor_csv.writerows(dados_pontos_analise)

with open('pontos.csv', 'r') as file:
    arquivo_csv = io.StringIO(file.read())

# Criar um FeatureSet usando o arquivo CSV
# feature_set = FeatureSet(features=pontos)


# Adicionar o arquivo CSV como um item no ArcGIS Online
item_properties = {
    "title": "Camada_de_Pontos_2",
    "tags": "pontos, GIS",
    "type": "CSV",
}

item_properties['fileName'] = 'pontos_2.csv'

item_name = "Camada_de_Pontos_2"

# Verifica se o item já existe
existing_items = gisEnter.content.search(query=f"title:{item_name}")

print('existing_items', existing_items)

if existing_items:
    # Se o item já existe, atualize-o
    # existing_item = existing_items[0]
    # existing_item.update(item_properties=item_properties, data=arquivo_csv)
    # existing_item.update({
    #     "spatialReference": {"wkid": 31983}  # Atualize com o wkid desejado
    # })
    for existing_item in existing_items:
        existing_item.delete()
    print(f"Item '{item_name}' deletado com sucesso.")

    # Se o item não existe, crie-o
csv_item = gisEnter.content.add(item_properties=item_properties, data=arquivo_csv, location_type="coordinates", coordinates_system={"wkid": 31983})

csv_item.publish()

print(f"Item '{item_name}' criado com sucesso.")

symbology = {
    "renderer": "SimpleRenderer",
    "symbol": {
        "color": [255, 0, 0, 128],  # Cor vermelha com 50% de transparência
        "size": 10,  # Tamanho do ponto
        "type": "esriSMS",
        "style": "esriSMSCircle"
    }
}

# Aplicar a simbologia à camada recém-publicada
csv_item.update({"drawingInfo": symbology})

print(f"Item '{item_name}' atualizado com sucesso.")

filteredData = gisEnter.content.search(query=f"title:{item_name}")

# filteredData2 = gisEnter.content.get("3624d6850b7642dd8ab3a8eddc570ffc")

print(filteredData)
# print(filteredData2)


# filteredData [<Item title:"Camada_de_Pontos" type:Feature Layer Collection owner:210033525>, <Item title:"Camada_de_Pontos" type:CSV owner:210033525>]

receivedData = ''

for data in filteredData:
    if data.type != 'CSV':
        receivedData = data

print('receivedData', receivedData)
print('receivedData', dir(receivedData))
print('receivedData-url', receivedData.id)

newFilteredData = gisEnter.content.get(receivedData.id)

print(newFilteredData)
print('newFilteredData', dir(newFilteredData))
print(newFilteredData.layers[0])

print('receivedData-url', receivedData.url)
print('receivedData-url', receivedData['url'])

# print("filteredData['layers']", filteredData['layers'])
# print('filteredData.layers', filteredData.layers)


# Create buffer

ports_buffer_5m = use_proximity.create_buffers(input_layer = newFilteredData.layers[0], distances=[5], units = 'Meters')

print(ports_buffer_5m)
print(dir(ports_buffer_5m))

# elements = ['geomAprx', 'nome', 'data']


# for item in pontos_dentro:
#     data = item['coordenada']
#     point_buffer5 = use_proximity.create_buffers(data, distances=[5], units = 'Meters')
#     buffer5_pontos_dentro.append({ 'type': point_buffer5, 'title': item.title })

# points_look = []

# for item in buffer5_pontos_dentro:

#     feature_ports_buffer5 = item.layer.featureSet.features
#     limit_feature_buffer5 = [feature.geometry for feature in feature_ports_buffer5]
#     limit_polygons_buffer5 = [Polygon(geom['rings'][0]) for geom in limit_feature_buffer5]



# feature_layer_item = gisAgo.content.add(item_properties=item_properties, data=feature_set)



# # Compartilhar a Feature Layer publicada
# feature_layer_item.share(everyone=True)

# print(f"Feature Layer publicada: {feature_layer_item.url}")

# feature_layer = gisAgo.content.import_data(camada_pontos_para_buffer)
# camada_pontos_para_buffer.save(gisAgo, "Camada_pre_buffer")
# camada_pontos_para_buffer.save(temp_path, out_name="Camada_pre_buffer")

# existing_layer = gisAgo.content.search("Camada_pre_buffer")
# if existing_layer:
#     existing_layer[0].delete()

# feature_layer = gisAgo.content.import_data(camada_pontos_para_buffer)
# # Salve a camada no ArcGIS Online
# # feature_layer.save(item_properties=item_properties, overwrite=True)

# print("URL do item:", item.url)
# print('pontos_dentro_lista_camada', camada_pontos_para_buffer)

# for item in pontos_dentro:
#     data = item['coordenada']
#     point_buffer5 = use_proximity.create_buffers(data, distances=[5], units = 'Meters')
#     buffer5_pontos_dentro.append({ 'type': point_buffer5, 'title': item.title })


# print('buffer5_pontos_dentro', buffer5_pontos_dentro)

#                                 # feature buffer

# points_look = []

# for item in buffer5_pontos_dentro:

#     feature_ports_buffer5 = item.layer.featureSet.features
#     limit_feature_buffer5 = [feature.geometry for feature in feature_ports_buffer5]
#     limit_polygons_buffer5 = [Polygon(geom['rings'][0]) for geom in limit_feature_buffer5]

#     if item.title == 'Árvores do Campus':
#         for i in limit_polygons_buffer5:
#             for y in myEnterGroupContent.content()[0]:
#                 if i.contains(y):
#                     points_look.append(y)


# print(points_look)

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