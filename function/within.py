from shapely.geometry import Point
# import pyproj
from pyproj import Transformer
import json
# import sys
# sys.path.append('/media/fortunato/F23ED4243ED3DFA117/Mestrado/develop')

# print(sys.path)
# from connection.conn_ago import connection_ago

# definir projeções
transformer = Transformer.from_crs("EPSG:102100", "EPSG:31983")
transformer_geojson = Transformer.from_crs("EPSG:102100", "EPSG:4326")


# def within_unb(point, limit_polygons):

#     ponto = point.geometry['x'], point.geometry['y']

#     x_transformed, y_transformed = transformer.transform(ponto[0], ponto[1])

#     ponto_shapely = Point(x_transformed, y_transformed)
    
#     dentro = False
#     for polygon in limit_polygons:
#         if ponto_shapely.within(polygon):
#             dentro = True
#             break
#     if dentro:
#         return True
#     else:
#         return False

# def within_build(point, limit_polygons):

#     #pega coordenada do ponto
#     ponto = point.geometry['x'], point.geometry['y']
#     #transforma a coordenada do ponto
#     x_transformed, y_transformed = transformer.transform(ponto[0], ponto[1])
#     #torna a coordenada do ponto geográfico
#     ponto_shapely = Point(x_transformed, y_transformed)
    
#     dentro = False
#     for polygon in limit_polygons:
#         if ponto_shapely.within(polygon):
#             dentro = True
#             break
#     if dentro:
#         return True
#     else:
#         return False
    
def function_within(point, limit_polygons):

    #pega coordenada do ponto
    ponto = point.geometry['x'], point.geometry['y']
    #transforma a coordenada do ponto
    x_transformed, y_transformed = transformer.transform(ponto[0], ponto[1])
    #torna a coordenada do ponto geográfico
    ponto_shapely = Point(x_transformed, y_transformed)
    
    dentro = False
    for polygon in limit_polygons:
        if ponto_shapely.within(polygon):
            dentro = True
            break
    if dentro:
        return True
    else:
        return False
    


def convert_json_geojson(name, json_data):
    features = []

    for point in json_data:
        #pega coordenada do ponto
        ponto = point['geometry']['x'], point['geometry']['y']
        #transforma a coordenada do ponto
        x_transformed, y_transformed = transformer_geojson.transform(ponto[0], ponto[1])

        feature = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [y_transformed, x_transformed],
          },
          "properties": point['attributes'],
        }
        features.append(feature)

    # return features

    #Objeto GeoJSON
    geojson_data = {
      "type": "FeatureCollection",
      "features": features
  }

    # Convertendo para string
    geojson_string = json.dumps(geojson_data)

    # return geojson_string

#     # Salvando em um arquivo
    with open(f'{name}.geojson', 'w') as f:
      f.write(geojson_string)