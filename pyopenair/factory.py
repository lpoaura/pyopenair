#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict

from shapely.wkt import loads

from pyopenair.helper import generate_coords

def wkt2openair(wkt, label="defaultlabel") -> str:
    """Return openair Coordinates from polygon or multipolygon

    :param wkt: Polygon or Multipolygon object as WKT with WGS84 projection
    :type wkt: str
    :param label: Geo object label, default is "defaullabel"
    :type label: str, optional
    :return: OpenAir string
    :rtype: str
    """
    header_template = """
AC C
AN {}
AL SFC

"""

    #     logging.debug('prepare to transform object named {}'.format(label))
    geom = loads(wkt)
    #     logging.debug('geom type is {}'.format(geom.geom_type))
    if geom.geom_type == "Polygon":
        node_coords = []
        #         print(list(geom.exterior.coords))
        for node in list(geom.exterior.coords):
            node_coords.append(generate_coords(node))
            node_coords = list(OrderedDict.fromkeys(node_coords))
        desc = header_template.format(label)
        for coord in node_coords:
            desc += "{}\n".format(coord)
        return desc
    if geom.geom_type == "MultiPolygon":
        result = ""
        i = 1
        for g in geom:
            node_coords = []
            for node in list(g.exterior.coords):
                #                 print(node)
                node_coords.append(generate_coords(node))
                node_coords = list(OrderedDict.fromkeys(node_coords))
            label_unit = "{}#{}".format(label, i)
            i = i + 1
            desc = header_template.format(label_unit)
            for coord in node_coords:
                desc += "{}\n".format(coord)
            result += desc

        return result

