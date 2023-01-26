import logging

from sample_data import BasicDataToTest, DataToTest, WKT_MULTIPOLY, WKT_POLY

from pyopenair.factory import wkt2openair

logger = logging.getLogger(__name__)


# class BasicDataToTest(NamedTuple):
#     wkt: str
#     an: str = "label"
#     ac: str = "class"


# class DataToTest(NamedTuple):
#     wkt: str
#     an: str = "label"
#     ac: str = "class"
#     al_alti: int = 100
#     al_unit: str = "m"
#     al_mode: str = "AGL"
#     ah_alti: int = 1000
#     ah_unit: str = "m"
#     ah_mode: str = "AGL"


# wktpoly = "POLYGON((3.85949710384011 44.6745125533035,3.82379153743386 44.5787302437756,3.96661380305886 44.5180516500055,4.01605227962136 44.5826428195841,3.96661380305886 44.6784186781885,3.85949710384011 44.6745125533035))"
# wktmultipoly = "MULTIPOLYGON(((4.36423688809855 44.3711532565767,4.33496656347426 44.3243697013707,4.39636764710812 44.3034034517409,4.44767104348119 44.3660466322347,4.39032381481851 44.4011336006027,4.36423688809855 44.3711532565767)),((4.24706792369804 44.5079123913788,4.24619170613213 44.468186176919,4.35772605055038 44.4520521267275,4.29510144795417 44.5093795504602,4.24706792369804 44.5079123913788)))"
# # an = "label"
# # ac = "class"
# # al_alti = 100
# # al_unit = "m"
# # al_mode = "AGL"
# # ah_alti = 1000
# # ah_unit = "m"
# # ah_mode = "AGL"


def test_wkt2openair_poly_only_required():
    """
    Test wkt2openair with polygon
    """

    openair = """AC class
AN label
DP 44:40:28 N 03:51:34 E
DP 44:34:43 N 03:49:25 E
DP 44:31:04 N 03:57:59 E
DP 44:34:57 N 04:00:57 E
DP 44:40:42 N 03:57:59 E"""
    assert wkt2openair(**(BasicDataToTest(WKT_POLY)._asdict())) == openair


def test_wkt2openair_poly():
    """
    Test wkt2openair with polygon
    """

    openair = """AC class
AN label
AH 3281FT AGL
AL 328FT AGL
DP 44:40:28 N 03:51:34 E
DP 44:34:43 N 03:49:25 E
DP 44:31:04 N 03:57:59 E
DP 44:34:57 N 04:00:57 E
DP 44:40:42 N 03:57:59 E"""
    assert wkt2openair(**(DataToTest(WKT_POLY)._asdict())) == openair


def test_wkt2openair_multipoly():
    """
    Test wkt2openair with polygon
    """

    openair = """AC class
AN label (1/2)
AH 3281FT AGL
AL 328FT AGL
DP 44:22:16 N 04:21:51 E
DP 44:19:27 N 04:20:05 E
DP 44:18:12 N 04:23:46 E
DP 44:21:57 N 04:26:51 E
DP 44:24:04 N 04:23:25 E


AC class
AN label (2/2)
AH 3281FT AGL
AL 328FT AGL
DP 44:30:28 N 04:14:49 E
DP 44:28:05 N 04:14:46 E
DP 44:27:07 N 04:21:27 E
DP 44:30:33 N 04:17:42 E

"""
    assert wkt2openair(**(DataToTest(WKT_MULTIPOLY)._asdict())) == openair
