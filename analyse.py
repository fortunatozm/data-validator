from connection.conn_ago import connection_ago
from function.within import function_within, convert_json_geojson
from function.analyse_feature import analyse_function
from shapely.geometry import Polygon
import json
import geopandas as gpd

from arcgis.features import Feature, FeatureSet, FeatureCollection
from arcgis.geometry import Geometry

gisAgo = connection_ago('fortunatompongo_UnB', 'EuamoaKelly1994')

print('gisAgo', gisAgo)

base_field_map = gisAgo.content.get('a75dd851c6d5436cb01a0ceaaa2a9013')

# pega a camada limite unb
limite_unb_oficial = gisAgo.content.get('0dc1a7598ca04fc5971440b8875ec6d4').layers[0]
limit_features_unb = limite_unb_oficial.query().features
# pega geometry da camada
limit_geometries_unb = [feature.geometry for feature in limit_features_unb]
# pega rings da peometria
limit_polygons_unb = [Polygon(geom['rings'][0]) for geom in limit_geometries_unb]

# pega a camada edificações unb
predio_unb = gisAgo.content.get('bc0e757ae4764d008d9cf1a0d296d7bc').layers[0]
limit_features_build = predio_unb.query().features
# pega geometry da camada
limit_geometries_build = [feature.geometry for feature in limit_features_build]
# pega rings da peometria
limit_polygons_build = [Polygon(geom['rings'][0]) for geom in limit_geometries_build]

# pega a camada escionamentos unb
estacionamento_unb = gisAgo.content.get('6cf17a0d1c7949f8ac1c415834a99019').layers[0]
limit_features_estacionamento = estacionamento_unb.query().features
# pega geometry da camada
limit_geometries_estacionamento = [feature.geometry for feature in limit_features_estacionamento]
# pega rings da peometria
limit_polygons_estacionamento = [Polygon(geom['rings'][0]) for geom in limit_geometries_estacionamento]

# pega a camada escionamentos unb
teste0 = gisAgo.content.get('01d3266c2592440ba4fc5f3a26c0dd43').layers[0]
teste = estacionamento_unb.query().features

# print('teste', teste)
# pega geometry da camada
teste2 = [feature.geometry for feature in teste]
# pega rings da peometria
teste3 = [Polygon(geom['rings'][0]) for geom in teste2]

# estacionamentos 6cf17a0d1c7949f8ac1c415834a99019
# estacionamentos completos 01d3266c2592440ba4fc5f3a26c0dd43

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

# print('new_list', new_list)

print('postes', all_nones)

all_features = ['postes', 'arvores', 'pontos_seguranca', 'estacionamentos', 'edificacoes']

poste_lista = ['geometriaAproximada', 'tipoPoste']


# Análises -------------------------------------------------------------------------------------

    # postes

analyse_postes = analyse_function('postes', all_postes, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)

    # arvores

analyse_arvores = analyse_function('arvores', all_arvores, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)

    # pontos de seguranca

analyse_ps = analyse_function('pontos_seguranca', all_pontos_seguranca, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)

    # estacionamentos

analyse_estacionamentos = analyse_function('estacionamentos', all_estacionamentos, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)
    
    # Coletores para reciclagem

analyse_coletoresparareciclagem = analyse_function('coletoresparareciclagem', all_coletoresparareciclagem, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Coletores de lixo

analyse_coletoresd_lixo = analyse_function('coletoresd_lixo', all_coletoresd_lixo, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Containers de Sala

analyse_containersdesala = analyse_function('containersdesala', all_containersdesala, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Conteiner de residuos

analyse_conteiner_residuos = analyse_function('conteiner_residuos', all_conteiner_residuos, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Bueiros

analyse_drenagem_bueiros = analyse_function('drenagem_bueiros', all_drenagem_bueiros, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Boca de lobo

analyse_drenagem_bocas_lobo = analyse_function('drenagem_bocas_lobo', all_drenagem_bocas_lobo, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Esgoto

analyse_esgoto_componentes = analyse_function('esgoto_componentes', all_esgoto_componentes, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Bacia de drenagem

analyse_drenagem_bacia_pe = analyse_function('drenagem_bacia_pe', all_drenagem_bacia_pe, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Água de amarrações

analyse_agua_amarracoes = analyse_function('agua_amarracoes', all_agua_amarracoes, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Refletores

analyse_refletores = analyse_function('refletores', all_refletores, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Subestações de energias

analyse_subestacoesdeenergias = analyse_function('subestacoesdeenergias', all_subestacoesdeenergias, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Torre de transmissão

analyse_torredetransmissao = analyse_function('torredetransmissao', all_torredetransmissao, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Iluminação pública

analyse_energia_iluminacao_publica = analyse_function('energia_iluminacao_publica', all_energia_iluminacao_publica, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Edificações

analyse_edificacoes = analyse_function('edificacoes', all_edificacoes, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Parada de Onibus

analyse_parada_onibus = analyse_function('parada_onibus', all_parada_onibus, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Escultura

analyse_escultura = analyse_function('escultura', all_escultura, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)    
    
    # Nones

analyse_nones = analyse_function('nones', all_nones, poste_lista, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento)

    # lista somada
listasomada = analyse_postes + analyse_arvores + analyse_ps + analyse_estacionamentos + analyse_coletoresparareciclagem + analyse_coletoresd_lixo + analyse_containersdesala + analyse_conteiner_residuos + analyse_drenagem_bueiros + analyse_drenagem_bocas_lobo + analyse_esgoto_componentes + analyse_drenagem_bacia_pe + analyse_agua_amarracoes + analyse_refletores + analyse_subestacoesdeenergias + analyse_torredetransmissao + analyse_energia_iluminacao_publica + analyse_edificacoes + analyse_parada_onibus + analyse_escultura + analyse_nones

# Mostrar detalhes

print('analyse_postes', type(analyse_postes[0]))
print('analyse_arvores', analyse_arvores)
print('analyse_arvores', type(analyse_arvores))
# print(all_postes[1])
print('analyse_ps', analyse_ps[0])
print('analyse_estacionamentos', analyse_estacionamentos[0])

# Pblicar --------------------------------------------------------------------------------

    # Poste -------------------------------------------------------------------------------

item_poste_name = 'Poste avaliado'

poste_data = convert_json_geojson(item_poste_name, analyse_postes)

# Leitura do arquivo GeoJSON
file_publish = f"{item_poste_name}.geojson"


poste_properties = {
    'title': item_poste_name,
    'type': 'GeoJson',
    'tags': 'poste, smart camous, UnB',
    'description': 'Camada avaliada'
}

# Verifica se o item já existe
    # Feature Layer
existing_poste_name = gisAgo.content.search(query=f"title:{item_poste_name}")

if existing_poste_name:
    for existing_item in existing_poste_name:
        if existing_item.owner == 'fortunatompongo_UnB':
            existing_item.delete()
    print(f"Item '{item_poste_name}' deletado com sucesso.")

    # Adicionar o item no ArcGIS Online
item_poste = gisAgo.content.add(item_properties=poste_properties, data=file_publish)

    # Publicar o item
published_poste_item = item_poste.publish()

    # Arvore ---------------------------------------------------------------------------

item_arvore_name = 'Arvore avaliada'

arvore_data = convert_json_geojson(item_arvore_name, analyse_arvores)

# Leitura do arquivo GeoJSON
file_arvore_publish = f"{item_arvore_name}.geojson"


arvore_properties = {
    'title': item_arvore_name,
    'type': 'GeoJson',
    'tags': 'arvore, smart camous, UnB',
    'description': 'Camada avaliada'
}

# Verifica se o item já existe
    # Feature Layer
existing_arvore_name = gisAgo.content.search(query=f"title:{item_arvore_name}")

if existing_arvore_name:
    for existing_item in existing_arvore_name:
        if existing_item.owner == 'fortunatompongo_UnB':
            existing_item.delete()
    print(f"Item '{item_arvore_name}' deletado com sucesso.")

    # Adicionar o item no ArcGIS Online
item_arvore = gisAgo.content.add(item_properties=arvore_properties, data=file_arvore_publish)

    # Publicar o item
published_item = item_arvore.publish()


    # Lista Somada ------------------------------------------------------------------------

item_all_name = 'Todos os dados coletados'

all_data = convert_json_geojson(item_all_name, listasomada)

# Leitura do arquivo GeoJSON
file_all_publish = f"{item_all_name}.geojson"


all_properties = {
    'title': item_all_name,
    'type': 'GeoJson',
    'tags': 'arvore, smart camous, UnB',
    'description': 'Camada avaliada'
}

# Verifica se o item já existe
    # Feature Layer
existing_all_name = gisAgo.content.search(query=f"title:{item_all_name}")

if existing_all_name:
    for existing_item in existing_all_name:
        if existing_item.owner == 'fortunatompongo_UnB':
            existing_item.delete()
    print(f"Item '{item_all_name}' deletado com sucesso.")

    # Adicionar o item no ArcGIS Online
item_all = gisAgo.content.add(item_properties=all_properties, data=file_all_publish)

    # Publicar o item
published_item = item_all.publish()