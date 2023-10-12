#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv
    argc = len(args)

    print(f"{argc - 1} argument{'' if (argc - 1) == 1 else 's'}{'.' if (argc - 1) == 0 else ':'}")

    for arg in args:
        if args.index(arg) != 0:
            print("{}: {}".format(args.index(arg), arg))
