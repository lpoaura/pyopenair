#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

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


def stringify_coords(value: any, strlength: int = 2) -> str:
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


def decdeg2dms(dd: any) -> tuple:
    """Convert decimal degree coordinate to a tuple containing each DMS values

    :param dd: Input value, can be string, float or integer
    :type dd: any
    :return: A tuple containing respectively degree, minutes and seconds
    :rtype: tuple
    """
    dd = float(dd)
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


def generate_openair_coord(coord: float, axis_type: str) -> str:
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


def generate_coords(coords: tuple) -> str:
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


def altitude_formatter(cat: str, alti: int, unit: str = "m", mode: str = None) -> any:
    """Airspace upper or lower bounds formatter

    :param kind: Is upper (h) or lower (l) bound
    :type kind: str
    :param alti: [description]
    :type alti: int
    :param unit: [description], defaults to 'm'
    :type unit: str, optional
    :param mode: [description], defaults to None
    :type mode: str, optional
    :return: [description]
    :rtype: any
    """
    if alti is None and mode is None:
        return None
    else:
        cat = cat.upper()
        strlist = []
        if cat not in ("H", "L"):
            raise ValueError('altitude type must be "H" or "L"')
        strlist.append("A{}".format(cat))
        if alti is not None:
            unit = unit.upper()
            if unit not in ("FT", "M", "FL"):
                raise ValueError('Altitude unit type must be "FT", "M" or "FL"')
            if unit == "FL":
                stralti = "{unit}{alti}"
            else:
                stralti = "{alti}FT"
                if unit == "M":
                    alti = int(alti * 3.28084)

            strlist.append(stralti.format(unit=unit, alti=alti))
        if mode is not None:
            strlist.append("{mode}".format(mode=mode))
        return " ".join(strlist)


def fields_formatter(cat: str, *args: str) -> str:
    """AirSpace description formatter, use to generate description lines begenning with "A"

    :param cat: Category suffix like, e.g. AC, AN, *Atimes
    :type cat: str
    :return: Formatter string, e.g. AC ZMC
    :rtype: str
    """
    if cat.replace("*", "")[0].upper() != "A":
        raise ValueError("field category must start with A or *A")
    if len([*args]) == 0:
        raise ValueError("field category must containt at least one argument")
    strlist = [cat.upper()]
    strlist.extend([*args])

    return " ".join(strlist)


def comment_formatter(comment: str) -> str:
    """[summary]

    :param comment: [description]
    :type comment: str
    :return: [description]
    :rtype: str
    """
    lines = comment.split("\n")
    max_len = -1
    for l in lines:
        if len(l) > max_len:
            max_len = len(l)
    new_lines = []
    new_lines.append("*" * (max_len + 4))
    for line in lines:
        new_lines.append("* " + line.ljust(max_len) + " *")
    new_lines.append("*" * (max_len + 4))
    new_comment = "\n".join(new_lines)
    return new_comment


def coalesce(var: any, default: any = "default") -> any:
    """Return a default value if main value is None

    :param var: entry variable
    :type var: any

    :param default: default value
    :type default: any

    :return:  return default if var is null
    :rtype: any
    """
    return default if var is None else var
