import json


features = []

def convert_json_geojson(name, json_data):

  for item in json_data:
      feature = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [item.geometry['x'], item.geometry['y']],
          },
          "properties": item.attributes,
      }
      features.append(feature)

  # Objeto GeoJSON
  geojson_data = {
      "type": "FeatureCollection",
      "features": features
  }

  # Convertendo para string
  geojson_string = json.dumps(geojson_data)

  # Salvando em um arquivo
  with open(f'{name}.geojson', 'w') as f:
      f.write(geojson_string)
