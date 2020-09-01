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
    x = '{}:{}:{} {}'.format(stringfy_coords(xd, 3), stringfy_coords(xm), stringfy_coords(xs), ylabel)
    openair_coords = 'DP {} {}'.format(y, x)
    return openair_coords


