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

    Parameters
    ----------
    value : int
        Input value, can be string, float or integer
    charnum: int, optional
        string length, replacing spaces with 0 (default is 2)

    Raises
    ------
    ValueError
        If charnum value not like 2 or 3
    RuntimeError
        If an error occured while executing transformation

    Returns
    -------
    str
        a stringified string representing degree, minutes or seconds coordinate
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

    Parameters
    ----------
    dd : float
        Coordinate value (latitude or longitude)


    Returns
    -------
    tuple
        A tuple containing respectively degree, minutes and seconds
    """
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

    Parameters
    ----------
    coord : float
        Coordinate value (latitude or longitude)

    axis_type: str
        Axis definition, must be one of these values : x, lon, longitude, y, latitude, lat

    Returns
    -------
    str
        A string that represents coordinate in OpenAir format  "DD:MM:SS DIRECTION"

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

    Parameterss
    ----------
    coords tuple
        WGS84 X/Y Coordinates

    Returns
    -------
    str
        A string with coordinates converted in openair format
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


def wkt2openair(wkt, label="defaultlabel") -> str:
    """Return openair Coordinates from polygon or multipolygon"""
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
            print("type node", node)
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
