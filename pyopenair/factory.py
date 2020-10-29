#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from shapely.wkt import loads
from pyopenair.helper import (
    generate_coords,
    altitude_formatter,
    fields_formatter,
)


def wkt2openair(
    wkt: str,
    an: str = "defaultlabel",
    ac: str = "?",
    ah_alti: int = None,
    ah_unit: str = "FT",
    ah_mode: str = "AMSL",
    al_alti: int = None,
    al_unit: str = "FT",
    al_mode: str = "SFC",
    other: dict = {},
) -> str:
    """Return an AirSpace in OpenAir format all main informations (name, class, upper and lower bounds, etc.)

    :param wkt: Object geometry as WGS84 (EPSG84:4326) WKT (only Polygon and Multipolygon are accepted)
    :type wkt: str
    :param an: Airspace name, defaults to "defaultlabel"
    :type an: str, optional
    :param ac: Airspace class, defaults to ""
    :type ac: str, optional
    :param ah_alti: Airspace upper bound altitude, defaults to None
    :type ah_alti: int, optional
    :param ah_unit: Airspace upper bound unit, defaults to "m"
    :type ah_unit: str, optional
    :param ah_mode: Airspace upper bound mode (AMSL, AGL, etc.), defaults to "AMSL"
    :type ah_mode: str, optional
    :param al_alti: Airspace lower bound altitude, defaults to None
    :type al_alti: int, optional
    :param al_unit: Airspace lower bound unit, defaults to "m"
    :type al_unit: str, optional
    :param al_mode: Airspace lower bound mode (?), defaults to "SFC"
    :type al_mode: str, optional
    :param sb: [description], defaults to None
    :type sb: str, optional
    :return: Airspace in OpenAir format
    :rtype: str
    """

    header = []
    header.append(fields_formatter("AC", ac))
    header.append(fields_formatter("AN", ac))
    header.append(altitude_formatter("H", ah_alti, ah_unit, ah_mode))
    header.append(altitude_formatter("L", al_alti, al_unit, al_mode))
    for k, v in other.items():
        header.append(fields_formatter(k, v))
    header.append("\n")
    #     logging.debug('prepare to transform object named {}'.format(label))
    geom = loads(wkt)
    #     logging.debug('geom type is {}'.format(geom.geom_type))
    if geom.geom_type == "Polygon":
        node_coords = []
        #         print(list(geom.exterior.coords))
        for node in list(geom.exterior.coords):
            node_coords.append(generate_coords(node))
            node_coords = list(OrderedDict.fromkeys(node_coords))
        desc = "\n".join(header)
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
