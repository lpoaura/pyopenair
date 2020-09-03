import logging
from collections import OrderedDict

from shapely.wkt import loads

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')


def stringfy_coords(value, charnum=2):
    """
    """
    result = str(int(value)).rjust(charnum, "0")
    return result


def decdeg2dms(dd):
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


def get_cardinal(coord, axis):
    pass


def generate_coords(coords):
    if coords[1] < 0:
        ylabel = 'S'
    else:
        ylabel = 'N'
    yd, ym, ys = decdeg2dms(coords[1])
    y = '{}:{}:{} {}'.format(stringfy_coords(yd), stringfy_coords(ym), stringfy_coords(ys), ylabel)
    if coords[0] < 0:
        xlabel = 'W'
    else:
        xlabel = 'E'
    xd, xm, xs = decdeg2dms(coords[0])
    x = '{}:{}:{} {}'.format(stringfy_coords(xd, 3), stringfy_coords(xm), stringfy_coords(xs), xlabel)
    openair_coords = 'DP {} {}'.format(y, x)
    return openair_coords


def wkt2openair(wkt, label='defaultlabel'):
    """Return openair Coordinates from polygon or multipolygon"""
    header_template = """
AC C
AN {}
AL SFC

"""

    #     logging.debug('prepare to transform object named {}'.format(label))
    geom = loads(wkt)
    #     logging.debug('geom type is {}'.format(geom.geom_type))
    if geom.geom_type == 'Polygon':
        node_coords = []
        #         print(list(geom.exterior.coords))
        for node in list(geom.exterior.coords):
            print(node)
            node_coords.append(generate_coords(node))
            node_coords = list(OrderedDict.fromkeys(node_coords))
        desc = header_template.format(label)
        for coord in node_coords:
            desc += '{}\n'.format(coord)
        return desc
    if geom.geom_type == 'MultiPolygon':
        result = ''
        i = 1
        for g in geom:
            node_coords = []
            for node in list(g.exterior.coords):
                #                 print(node)
                node_coords.append(generate_coords(node))
                node_coords = list(OrderedDict.fromkeys(node_coords))
            label_unit = '{}#{}'.format(label, i)
            i = i + 1
            desc = header_template.format(label_unit)
            for coord in node_coords:
                desc += '{}\n'.format(coord)
            result += desc

        return result
