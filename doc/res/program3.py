#!/usr/bin/env python


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    # mandatory x value, no prefix
    parser.add_argument("x", type=int, help="The x value")
    # optional y value
    parser.add_argument("--y", type=int, help="The optional y value", default=42)
    # "negate"-flag
    parser.add_argument("--negate", action="store_true", help="Should x be negated?")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print("Arguments: %s" % args)

    x = args.x
    if args.negate:
        x = -x
    result = x + args.y
    print("Result: %f" % result)
