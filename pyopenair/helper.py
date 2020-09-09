#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from collections import OrderedDict

from shapely.wkt import loads

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(format="%(process)d-%(levelname)s-%(message)s")

AXIS_DICT = {
    "longitude": "x",
    "lon": "x",
    "x": "x",
    "latitude": "y",
    "lat": "y",
    "y": "y",
}

AXIS_DIR_DICT = {"y": ["N", "S"], "x": ["E", "W"]}

COORDS_ORDER = ["x", "y"]


def stringify_coords(value, strlength=2) -> str:
    """Stringify  each DMS integer values to formatted strings. eg: 6 seconds will return 006

    :param value: Input value, can be string, float or integer
    :type value: any
    :param strlength: string length, replacing spaces with 0, defaults is 2
    :type strlength: int, optional
    :raises ValueError: If charnum value not like 2 or 3
    :raises RuntimeError: If an error occured while executing transformation
    :return: a stringified string representing degree, minutes or seconds coordinate
    :rtype: str
    """

    strlength_valid = [2, 3]
    if strlength not in strlength_valid:
        raise ValueError(
            "<stringify_coords> strlength value must be one of {}".format(charnum_valid)
        )
    try:
        result = str(int(float(value))).rjust(strlength, "0")
        return result
    except Exception as e:
        raise RuntimeError("<stringify_coords> failed for reason: {}".format(e))


def decdeg2dms(dd) -> tuple:
    """Convert decimal degree coordinate to a tuple containing each DMS values

    :param dd: Input value, can be string, float or integer
    :type dd: any
    :return: A tuple containing respectively degree, minutes and seconds
    :rtype: tuple
    """
    dd=float(dd)
    negative = dd < 0
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return (degrees, minutes, seconds)


def generate_openair_coord(coord, axis_type) -> str:
    """Generate coordinate in openair format "DD:MM:SS DIRECTION"

    :param coord: Coordinate value (latitude or longitude)
    :type coord: float
    :param axis_type: Axis definition, must be one of these values : x, lon, longitude, y, latitude, lat
    :type axis_type: str
    :return: A string that represents coordinate in OpenAir format  "DD:MM:SS DIRECTION"
    :rtype: str
    """

    if axis_type not in AXIS_DICT.keys():
        raise ValueError(
            "<get_cardinal> strlength value must be one of {}".format(AXIS_DICT.keys())
        )

    axis = AXIS_DICT[axis_type]

    if coord < 0:
        label = AXIS_DIR_DICT[axis][1]
    else:
        label = AXIS_DIR_DICT[axis][0]
    d, m, s = decdeg2dms(coord)
    coord = "{}:{}:{} {}".format(
        stringify_coords(d), stringify_coords(m), stringify_coords(s), label
    )
    return coord


def generate_coords(coords) -> str:
    """Generate X/Y coordinates in OpenAir format "DP DD:MM:SS N DD:MM:SS E"

    :param coords: Axis definition, must be one of these values : x, lon, longitude, y, latitude, lat
    :type coords: tuple
    :return:  A string with coordinates converted in openair format
    :rtype: str
    """
    if type(coords) is not tuple:
        raise TypeError("<generate_coords> coords must be a tuple")
    if len(coords) != 2:
        raise ValueError("<generate_coords> coords must be a tuple of 2 values")
    openair_coord = ()
    for i in range(len(COORDS_ORDER)):
        if abs(coords[i]) > 180:
            raise ValueError(
                "<generate_coords> decimal coords must be between 0 and 180°, value for {} is {}".format(
                    COORDS_ORDER[i], coords[i]
                )
            )
        else:
            openair_coord = openair_coord + (
                generate_openair_coord(coords[i], COORDS_ORDER[i]),
            )
    openair_coords = "DP {} {}".format(openair_coord[1], openair_coord[0])
    return openair_coords

