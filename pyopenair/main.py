#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Main """

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
    optional_parser = parser._action_groups.pop()  # Edited this line
    # optional_parser = parser.add_argument_group("optional named arguments")

    required_parser = parser.add_argument_group("required arguments")
    required_parser.add_argument(
        "--wkt",
        metavar="wkt",
        required=True,
        help="Airspace geometry as WKT in WGS84",
    )
    required_parser.add_argument(
        "--ac", metavar="class", required=True, help="Airspace class"
    )
    optional_parser.add_argument(
        "--an", metavar="label", required=False, help="Airspace name"
    )
    optional_parser.add_argument(
        "--al_alti", metavar="al_alti", required=False, help="AL altitude"
    )
    optional_parser.add_argument(
        "--al_unit",
        metavar="al_unit",
        required=False,
        help="AL Altitude unit",
    )
    optional_parser.add_argument(
        "--al_mode",
        metavar="al_mode",
        required=False,
        help="AL Altitude mode",
    )
    optional_parser.add_argument(
        "--ah_alti", metavar="ah_alti", required=False, help="AH altitude"
    )
    optional_parser.add_argument(
        "--ah_unit",
        metavar="ah_unit",
        required=False,
        help="AH Altitude unit",
    )
    optional_parser.add_argument(
        "--ah_mode",
        metavar="ah_mode",
        required=False,
        help="AH Altitude mode",
    )
    optional_parser.add_argument(
        "--comment", metavar="comment", required=False, help="Comment"
    )
    parser._action_groups.append(optional_parser)  # added this line
    args = parser.parse_args()

    # logging.basicConfig(level=args.logLevel)

    logging.basicConfig(
        format="%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s",
        level=args.loglevel,
    )
    logger = logging.getLogger(__name__)
    # logger.debug(f"logLevel {args.logLevel} d{logging.DEBUG} i{logging.INFO}")
    logger.debug(
        "Args \n%s",
        "\n".join(
            [f"\t{key}: {value}" for key, value in sorted(vars(args).items())]
        ),
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
