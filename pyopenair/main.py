from .factory import wkt2openair
import argparse
from . import __version__


def cli():
    """PyOpenair command line interface"""
    parser = argparse.ArgumentParser(
        description=f"""\
Convert wkt to openair
----------------------
    version:  {__version__}
    source code: https://github.com/lpoaura/pyopenair
    documentation: https://pyopenair.readthedocs.io
""",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    optionalParser = parser._action_groups.pop()  # Edited this line
    # optionalParser = parser.add_argument_group("optional named arguments")

    requiredParser = parser.add_argument_group("required arguments")
    requiredParser.add_argument(
        "--wkt",
        metavar="wkt",
        required=True,
        help="Airspace geometry as WKT in WGS84",
    )
    requiredParser.add_argument(
        "--ac", metavar="class", required=True, help="Airspace class"
    )
    optionalParser.add_argument(
        "--an", metavar="label", required=False, help="Airspace name"
    )
    optionalParser.add_argument(
        "--al_alti", metavar="al_alti", required=False, help="AL altitude"
    )
    optionalParser.add_argument(
        "--al_unit",
        metavar="al_unit",
        required=False,
        help="AL Altitude unit",
    )
    optionalParser.add_argument(
        "--al_mode",
        metavar="al_mode",
        required=False,
        help="AL Altitude mode",
    )
    optionalParser.add_argument(
        "--ah_alti", metavar="ah_alti", required=False, help="AH altitude"
    )
    optionalParser.add_argument(
        "--ah_unit",
        metavar="ah_unit",
        required=False,
        help="AH Altitude unit",
    )
    optionalParser.add_argument(
        "--ah_mode",
        metavar="ah_mode",
        required=False,
        help="AH Altitude mode",
    )
    optionalParser.add_argument(
        "--comment", metavar="comment", required=False, help="Comment"
    )
    parser._action_groups.append(optionalParser)  # added this line
    args = parser.parse_args()
    print(
        wkt2openair(
            wkt=args.wkt,
            an=args.an,
            ac=args.ac,
            al_alti=args.al_alti,
            al_unit=args.al_unit,
            al_mode=args.al_mode,
            ah_alti=args.ah_alti,
            ah_unit=args.ah_unit,
            ah_mode=args.ah_mode,
            comment=args.comment,
        )
    )
    return args


if __name__ == "__main__":
    cli()
