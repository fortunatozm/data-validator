from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from arcgis.geometry import Point

# Conectar-se ao ArcGIS Online
gis = GIS("https://www.arcgis.com", "username", "password")

# Obter a camada de feições
feature_layer = FeatureLayer("url_da_sua_camada_de_feicoes")

# Consultar todos os pontos
query_result = feature_layer.query(where="1=1", return_geometry=True)

# Criar um dicionário para armazenar os pontos sobrepostos
overlapping_points = {}

# Iterar sobre os pontos e verificar sobreposição
for feature in query_result.features:
    point1 = feature.geometry
    for existing_feature in overlapping_points.keys():
        point2 = existing_feature.geometry
        if point1.distance(point2) <= 5:
            # Se os pontos estiverem dentro do raio de 5 metros, adicione-os ao dicionário
            overlapping_points[existing_feature].append(feature)
            break
    else:
        # Se não houver sobreposição, adicione o ponto ao dicionário
        overlapping_points[feature] = []

# Excluir um dos pontos sobrepostos
for existing_feature, overlapping_features in overlapping_points.items():
    if len(overlapping_features) > 0:
        # Excluir o primeiro ponto sobreposto encontrado
        feature_to_delete = overlapping_features[0]
        result = feature_layer.edit_features(deletes=[feature_to_delete.attributes['OBJECTID']])
        if 'success' in result:
            print(f"Ponto excluído com sucesso: {feature_to_delete.attributes['OBJECTID']}")
        else:
            print(f"Erro ao excluir o ponto: {result}")
