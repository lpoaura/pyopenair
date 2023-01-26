"""sample data"""
from typing import NamedTuple


class BasicDataToTest(NamedTuple):
    """_summary_

    :param NamedTuple: _description_
    :type NamedTuple: _type_
    """

    wkt: str
    an: str = "label"
    ac: str = "class"


class DataToTest(NamedTuple):
    """_summary_

    :param BasicDataToTest: _description_
    :type BasicDataToTest: _type_
    """

    wkt: str
    an: str = "label"
    ac: str = "class"
    al_alti: int = 100
    al_unit: str = "m"
    al_mode: str = "AGL"
    ah_alti: int = 1000
    ah_unit: str = "m"
    ah_mode: str = "AGL"


HEADERS = ["AC class", "AH 3281FT AGL", "AN {label}", "AL 328FT AGL"]
WKT_POLY = "POLYGON((3.85949710384011 44.6745125533035,3.82379153743386 44.5787302437756,3.96661380305886 44.5180516500055,4.01605227962136 44.5826428195841,3.96661380305886 44.6784186781885,3.85949710384011 44.6745125533035))"
WKT_MULTIPOLY = "MULTIPOLYGON(((4.36423688809855 44.3711532565767,4.33496656347426 44.3243697013707,4.39636764710812 44.3034034517409,4.44767104348119 44.3660466322347,4.39032381481851 44.4011336006027,4.36423688809855 44.3711532565767)),((4.24706792369804 44.5079123913788,4.24619170613213 44.468186176919,4.35772605055038 44.4520521267275,4.29510144795417 44.5093795504602,4.24706792369804 44.5079123913788)))"
