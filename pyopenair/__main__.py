from .factory import wkt2openair

if __name__ == "__main__":
    # execute only if run as a script
    import argparse

    parser = argparse.ArgumentParser(description="convert wkt to openair")
    parser.add_argument(
        "--wkt", metavar="wkt", required=True, help="Geo object as WKT in WGS84"
    )
    parser.add_argument("--ac", metavar="label", required=True, help="Airspace class")
    parser.add_argument("--an", metavar="label", required=False, help="Geo object name")
    parser.add_argument("--comment", metavar="comment", required=False, help="Comment")
    args = parser.parse_args()
    print(wkt2openair(wkt=args.wkt, an=args.an, ac=args.ac, comment=args.comment))
