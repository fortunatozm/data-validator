from shapely.ops import nearest_points
from shapely.geometry import Point, Polygon
from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:102100", "EPSG:31983")

# distancia de um ponto com o ponto mais próximo de um poligono

def point_polygon_distance(point, polygon, max_limit):

    point_x_y = point.geometry['x'], point.geometry['y']
    x_transformed, y_transformed = transformer.transform(point_x_y[0], point_x_y[1])
    point_transformed = Point(x_transformed, y_transformed)
    # poligono = Polygon(polygon)
    # print('polygon', type (polygon))
    # print('point', type (point))
    # print('polygon', polygon)
    # print('point_transformed', point_transformed)
    # print('poligono', poligono)

    nearest_point_on_polygon, _ = nearest_points(polygon, point_transformed)

    # print('nearest_point_on_polygon', nearest_point_on_polygon)
    # print('polygon', polygon)

    distance = point_transformed.distance(nearest_point_on_polygon)

    # print('distance', distance.min(), distance.max())

    distance_min = distance.min()

    if distance_min <= max_limit:
        return True
    else:
        return False

# distancia entre dois pontos
    
def point_distance(point_1, point_2, max_limit):

    point_1_x_y = point_1.geometry['x'], point_1.geometry['y']
    point_1_x_transformed, point_1_y_transformed = transformer.transform(point_1_x_y[0], point_1_x_y[1])
    point_1_transformed = Point(point_1_x_transformed, point_1_y_transformed)
    
    point_2_x_y = point_2.geometry['x'], point_2.geometry['y']
    point_2_x_transformed, point_2_y_transformed = transformer.transform(point_2_x_y[0], point_2_x_y[1])
    point_2_transformed = Point(point_2_x_transformed, point_2_y_transformed)

    distance = point_1_transformed.distance(point_2_transformed)

    # print('distance', distance)
    if distance <= max_limit:
        return True
    else:
        return False
