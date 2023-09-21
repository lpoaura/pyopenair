#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Factory"""

import logging
from typing import Optional

from shapely.wkt import loads  # type: ignore

from .helper import (
    altitude_formatter,
    comment_formatter,
    fields_formatter,
    object_formatter,
)

logger = logging.getLogger(__name__)


def wkt2openair(
    wkt: str,
    an: str = "defaultlabel",
    ac: str = "?",
    ah_alti: Optional[int] = None,
    ah_unit: str = "FT",
    ah_mode: str = "AMSL",
    al_alti: Optional[int] = None,
    al_unit: str = "FT",
    al_mode: str = "SFC",
    comment: Optional[str] = None,
    other: Optional[dict] = None,
) -> Optional[str]:
    """Return an AirSpace in OpenAir format all main informations
    (name, class, upper and lower bounds, etc.)

    :param wkt: Object geometry as WGS84 (EPSG84:4326) WKT (Polygon and Multipolygon only)
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
    label = fields_formatter("AN", an)
    if comment:
        header.append(comment_formatter(comment))
    header.append(fields_formatter("AC", ac))
    header.append("{label}")
    if other:
        for key, value in other.items():
            header.append(fields_formatter(key, value))
    if ah_alti and ah_mode:
        ah_value = altitude_formatter("H", ah_alti, ah_unit, ah_mode)
        if ah_value:
            header.append(ah_value)
    al_value = None
    if al_alti or al_mode:
        al_value = altitude_formatter("L", al_alti, al_unit, al_mode)
        if al_value:
            header.append(al_value)
    obj = loads(wkt)
    if obj.geom_type == "Polygon":
        return object_formatter(obj, label, header)
    if obj.geom_type == "MultiPolygon":
        areas, len_geom, i = [], len(obj.geoms), 0
        for geom in obj.geoms:
            i += 1
            label_item = f"{label} ({i}/{len_geom})"
            desc = object_formatter(geom, label_item, header)
            desc += "\n\n"
            areas.append(desc)
        return "\n".join(areas)

    return None
