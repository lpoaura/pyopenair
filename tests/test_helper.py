from data import headers, wktpoly
from shapely.wkt import loads

from pyopenair.helper import (
    altitude_formatter,
    comment_formatter,
    decdeg2dms,
    fields_formatter,
    generate_coords,
    generate_openair_coord,
    object_formatter,
    stringify_coords,
)


def test_stringify_coords_l2():
    assert stringify_coords(1, 2) == "01"


def test_stringify_coords_l3():
    assert stringify_coords(1, 3) == "001"


def test_decdeg2dms():
    result = (5.0, 33.0, 18.0)
    assert decdeg2dms(5.555) == result


def test_upper_bounds_altitude_formatter_m():
    result = "AH 329FT AGL"
    assert (
        altitude_formatter(cat="H", alti=100, unit="m", mode="AGL") == result
    )


def test_upper_bounds_altitude_formatter_empty():
    result = None
    assert (
        altitude_formatter(cat="H", alti=None, unit=None, mode=None) == result
    )


def test_lower_bounds_altitude_formatter_empty():
    result = None
    assert (
        altitude_formatter(cat="L", alti=None, unit=None, mode=None) == result
    )


def test_lower_bounds_altitude_formatter_m():
    result = "AL 328FT AGL"
    assert (
        altitude_formatter(cat="L", alti=100, unit="m", mode="AGL") == result
    )


def test_altitude_formatter_ft():
    result = "AL 100FT AGL"
    assert (
        altitude_formatter(cat="l", alti=100, unit="ft", mode="AGL") == result
    )


def test_fields_formatter():
    result = "*ATYPE arg1 arg2"
    assert fields_formatter("*ATYPE", "arg1", "arg2") == result


def test_generate_openair_coord_x():
    result = "45:00:00 E"
    assert generate_openair_coord(45, "x") == result


def test_generate_openair_coord_y():
    result = "45:00:00 N"
    assert generate_openair_coord(45, "y") == result


def test_generate_openair_coord_lon():
    result = "45:00:00 E"
    assert generate_openair_coord(45, "longitude") == result


def test_generate_openair_coord_lat():
    result = "45:00:00 N"
    assert generate_openair_coord(45, "latitude") == result


def test_generate_coords():
    result = "DP 45:33:18 N 05:33:18 E"
    assert generate_coords((5.555, 45.555)) == result


def test_comment_formatter():
    comment = """A pariatur dignissimos vel ipsum pariatur
Veritatis eum aut aut dolorem doloremque reprehenderit
Dolor et dicta ducimus in provident quod.
"""
    result = "**********************************************************\n* A pariatur dignissimos vel ipsum pariatur              *\n* Veritatis eum aut aut dolorem doloremque reprehenderit *\n* Dolor et dicta ducimus in provident quod.              *\n*                                                        *\n**********************************************************"
    assert comment_formatter(comment) == result


def test_object_formatter():
    obj = object_formatter(loads(wktpoly), "labeldetest", headers)
    result = """AC class
AH 3281FT AGL
AN labeldetest
AL 328FT AGL
DP 44:40:28 N 03:51:34 E
DP 44:34:43 N 03:49:25 E
DP 44:31:04 N 03:57:59 E
DP 44:34:57 N 04:00:57 E
DP 44:40:42 N 03:57:59 E"""
    assert obj == result
