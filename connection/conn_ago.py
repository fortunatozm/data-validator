from arcgis.gis import GIS

urlAgo = 'https://www.arcgis.com'

def connection_ago(user, password):
  return GIS(urlAgo, user, password)

