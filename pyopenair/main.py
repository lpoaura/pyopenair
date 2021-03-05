import argparse
import logging

from . import __version__
from .factory import wkt2openair


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
    parser.add_argument(
        "--version", "-V", action="version", version="%(prog)s " + __version__
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="Debug mode",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
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

    # logging.basicConfig(level=args.logLevel)

    logging.basicConfig(
        format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s",
        level=args.loglevel,
    )
    logger = logging.getLogger(__name__)
    # logger.debug(f"logLevel {args.logLevel} d{logging.DEBUG} i{logging.INFO}")
    logger.debug(
        "Args \n{args}".format(
            args="\n".join(
                [
                    "\t{}: {}".format(k, v)
                    for k, v in sorted(vars(args).items())
                ]
            )
        )
    )

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
