#!/usr/bin/env python
if __name__ == "__main__":
    import sys
    for idx, arg in enumerate(sys.argv):
        print("Argument %2d: %s" % (idx, arg))
