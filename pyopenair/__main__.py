from .factory import wkt2openair

if __name__ == '__main__':
    # execute only if run as a script
    import argparse

    parser = argparse.ArgumentParser(description='convert wkt to openair')
    parser.add_argument('--wkt', metavar='wkt', required=True,
                        help='geo object as WKT in WGS84')
    parser.add_argument('--label', metavar='label', required=False,
                        help='geo object name')
    args = parser.parse_args()
    print(wkt2openair(wkt=args.wkt, label=args.label))
