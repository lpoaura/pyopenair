from .factory import wkt2openair

if __name__ == "__main__":
    # execute only if run as a script
    import argparse

    parser = argparse.ArgumentParser(description="convert wkt to openair")
    parser.add_argument(
        "--wkt", metavar="wkt", required=True, help="Airspace geometry as WKT in WGS84"
    )
    parser.add_argument("--ac", metavar="class", required=True, help="Airspace class")
    parser.add_argument("--an", metavar="label", required=False, help="Airspace name")
    parser.add_argument(
        "--al_alti", metavar="al_alti", required=False, help="AL altitude"
    )
    parser.add_argument(
        "--al_unit", metavar="al_unit", required=False, help="AL Altitude unit"
    )
    parser.add_argument(
        "--al_mode", metavar="al_mode", required=False, help="AL Altitude mode"
    )
    parser.add_argument(
        "--ah_alti", metavar="ah_alti", required=False, help="AH altitude"
    )
    parser.add_argument(
        "--ah_unit", metavar="ah_unit", required=False, help="AH Altitude unit"
    )
    parser.add_argument(
        "--ah_mode", metavar="ah_mode", required=False, help="AH Altitude mode"
    )
    parser.add_argument("--comment", metavar="comment", required=False, help="Comment")
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
