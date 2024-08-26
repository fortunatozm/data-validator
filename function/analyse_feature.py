from function.within import function_within
from function.distance import point_polygon_distance, point_distance


def analyse_function(feature_name, feature_points, attribute_list, limit_polygons_unb, limit_polygons_build, limit_polygons_estacionamento):

    data_after_analyse = []

    # Postes
    if feature_name == 'postes':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID'],
                    # 'tipocoleta': point.attributes['tipo_coleta'],
                    # 'Camada': coord['title']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    print('point_polygon_distance()', point_polygon_distance(point, limit_polygons_build, 2))
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        # Normalizando
                        ponto['attributes']['geoaprox'] = 'Sim'
                        ponto['attributes']['tipoposte'] = point.attributes['tipo_poste']
                        ponto['attributes']['tipomateria'] = point.attributes['materiapo']
                        ponto['attributes']['quantlamp'] = point.attributes['qde_lampadas']
                        ponto['attributes']['quantmaior1'] = point.attributes['qtde_maior_menor_um']
                        ponto['attributes']['potencialam'] = point.attributes['pt_Lampada']
                        ponto['attributes']['tipolampada'] = point.attributes['tp_Lampada']
                        ponto['attributes']['quantlumina'] = point.attributes['quantlumi']
                        ponto['attributes']['rede'] = point.attributes['rede']
                        ponto['attributes']['tiporede'] = point.attributes['tiporede']
                        ponto['attributes']['tiporede'] = point.attributes['tiporede']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Arvores
    if feature_name == 'arvores':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        # Normalizando
                        ponto['attributes']['tipoarvore'] = point.attributes['tipo_de_arvore']
                        ponto['attributes']['altura'] = point.attributes['altura']
                        ponto['attributes']['diametro'] = point.attributes['diametro']
                        ponto['attributes']['especie'] = point.attributes['espcie']
                        ponto['attributes']['familia'] = point.attributes['famlia']
                        ponto['attributes']['anomalia'] = point.attributes['anomalia']
                        ponto['attributes']['datapoda'] = point.attributes['datapoda']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)

    # Pontos de segurança
    if feature_name == 'pontos_seguranca':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Estacionamentos
    if feature_name == 'estacionamentos':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['publico'] = point.attributes['publico']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Coletores para reciclagem
    if feature_name == 'coletoresparareciclagem':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID'],
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['quantcolrec'] = point.attributes['Quantidade_de_coletores_de_reciclagem']
                        ponto['attributes']['tipomateria'] = point.attributes['coletores_de_reciclagem']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
    
    # Coletores de lixo
    if feature_name == 'coletoresd_lixo':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['quantcollix'] = point.attributes['Quantidade_de_coletores']
                        ponto['attributes']['tipomateria'] = point.attributes['Materialcoletorlixo']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
    
    # Containers de Sala
    if feature_name == 'containersdesala':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['altura'] = point.attributes['Altura_de_container']
                        ponto['attributes']['largura'] = point.attributes['Largura_do_container']
                        ponto['attributes']['profundidade'] = point.attributes['Profundidade_do_container']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)

    # Conteiner de residuos
    if feature_name == 'conteiner_residuos':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['cor'] = point.attributes['cor']
                        ponto['attributes']['normafabric'] = point.attributes['norma_fab']
                        ponto['attributes']['datainstala'] = point.attributes['data_instalacao']
                        ponto['attributes']['tipomateria'] = point.attributes['material']
                        ponto['attributes']['capacidade'] = point.attributes['capacidade']
                        ponto['attributes']['protecaouv'] = point.attributes['proteo_uv']
                        ponto['attributes']['tampaarticu'] = point.attributes['tampa_articular']
                        ponto['attributes']['munhulatera'] = point.attributes['munhoes_laterais']
                        ponto['attributes']['tiporoda'] = point.attributes['Tipo_de_roda']
                        ponto['attributes']['altura'] = point.attributes['altura_container']
                        ponto['attributes']['largura'] = point.attributes['largura_container']
                        ponto['attributes']['profundidad'] = point.attributes['profundidade']
                        ponto['attributes']['dreno'] = point.attributes['dreno']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)

    # Bueiros
    if feature_name == 'drenagem_bueiros':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Boca de lobo
    if feature_name == 'drenagem_bocas_lobo':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID'],
                    # 'tipocoleta': point.attributes['tipo_coleta'],
                    # 'Camada': coord['title']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Esgoto
    if feature_name == 'esgoto_componentes':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID'],
                    # 'tipocoleta': point.attributes['tipo_coleta'],
                    # 'Camada': coord['title']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Bacia de drenagem
    if feature_name == 'drenagem_bacia_pe':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)

    # Água de amarrações
    if feature_name == 'agua_amarracoes':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Refletores
    if feature_name == 'refletores':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Subestações de energias
    if feature_name == 'subestacoesdeenergias':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['tipomateria'] = point.attributes['Material_de_subestacao']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)

    # Torre de transmissão
    if feature_name == 'torredetransmissao':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)

    # Iluminação pública
    if feature_name == 'energia_iluminacao_publica':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                
    # Edificações
    if feature_name == 'edificacoes':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['nome'] = point.attributes['nomeedif']
                        ponto['attributes']['numpav'] = point.attributes['pavimentos']
                        ponto['attributes']['numsalas'] = point.attributes['salas']
                        ponto['attributes']['operacional'] = point.attributes['operacion']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)

    # Parada de Onibus
    if feature_name == 'parada_onibus':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['modaluso'] = point.attributes['modalsuo']
                        ponto['attributes']['situafisic'] = point.attributes['situafisic']
                        ponto['attributes']['operacional'] = point.attributes['operacionP']
                        ponto['attributes']['qrcode'] = point.attributes['qrcode']
                        ponto['attributes']['tipoexpo'] = point.attributes['tipoexpo']
                        ponto['attributes']['tipomateria'] = point.attributes['materialpa']
                        ponto['attributes']['assento'] = point.attributes['assento']
                        ponto['attributes']['estabilidade'] = point.attributes['estabilidade']
                        ponto['attributes']['linha'] = point.attributes['linha']
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
    
    # Escultura
    if feature_name == 'escultura':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
                         
    # Nones
    if feature_name == 'nones':

        for point in feature_points:

            ponto = {
                'geometry': {
                    'x': point.geometry['x'],
                    'y': point.geometry['y'],
                    'spatialReference': {'wkid': 102100}
                },
                'attributes': {
                    'OBJECTID': point.attributes['OBJECTID']
                    }
            }
                                
            if function_within(point, limit_polygons_unb):
                if function_within(point, limit_polygons_build):
                    ponto['attributes']['status'] = 'Pendente'
                    data_after_analyse.append(ponto)
                # elif function_within(point, limit_polygons_estacionamento) and  point_polygon_distance(point, limit_polygons_canteiro, 2):
                else:
                    # if all(chave in point.attributes for chave in attribute_list):
                    if all(chave in point.attributes and point.attributes[chave] != 'null' for chave in attribute_list):
                        ponto['attributes']['status'] = 'Aprovado'
                        data_after_analyse.append(ponto)
                    else:
                        ponto['attributes']['localizacao'] = point.attributes['localizaca']
                        ponto['attributes']['datacoleta'] = point.attributes['full_date']
                        ponto['attributes']['status'] = 'Normalizado'
                        data_after_analyse.append(ponto)
            else:
                ponto['attributes']['status'] = 'Rejeitado'
                data_after_analyse.append(ponto)
    
    return data_after_analyse