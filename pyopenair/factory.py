#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from collections import OrderedDict
from shapely.wkt import loads
from pyopenair.helper import (
    generate_coords,
    altitude_formatter,
    fields_formatter,
    comment_formatter,
)


logger = logging.getLogger(__name__)


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
    comment: str = None,
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
    logger.debug(
        "Locals: \n{locals}".format(
            locals="\n".join(
                ["\t{}: {}".format(k, v) for k, v in locals().items()]
            )
        )
    )
    header = []
    label = fields_formatter("AN", an)
    logger.debug("label: {label}".format(label=label))

    if comment:
        header.append(comment_formatter(comment))
    header.append(fields_formatter("AC", ac))
    header.append("{label}")
    for k, v in other.items():
        header.append(fields_formatter(k, v))
    if ah_alti and ah_mode:
        header.append(altitude_formatter("H", ah_alti, ah_unit, ah_mode))
    if al_alti and al_mode:
        header.append(altitude_formatter("L", al_alti, al_unit, al_mode))
    geom = loads(wkt)
    if geom.geom_type == "Polygon":
        node_coords = []
        for node in list(geom.exterior.coords):
            node_coords.append(generate_coords(node))
            node_coords = list(OrderedDict.fromkeys(node_coords))
        desc = "\n".join(header).format(label=label)
        for coord in node_coords:
            desc += "\n{}".format(coord)
        return desc
    elif geom.geom_type == "MultiPolygon":
        areas = []
        lengeom = len(geom)
        i = 1
        for g in geom:
            node_coords = []
            for node in list(g.exterior.coords):
                node_coords.append(generate_coords(node))
                node_coords = list(OrderedDict.fromkeys(node_coords))
            label_elem = "{} ({}/{})".format(label, i, lengeom)
            i = i + 1
            desc_tpl = "\n".join(header)
            desc = desc_tpl.format(label=label_elem)
            for coord in node_coords:
                desc += "\n{}".format(coord)
            desc += "\n\n"
            areas.append(desc)
            return "\n".join(areas)
    else:
        return None
