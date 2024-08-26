from arcgis.gis import GIS

urlEnter = 'https://ide.unb.br/portal/'

def connection_enter(user, password):
  return GIS(urlEnter, user, password)

