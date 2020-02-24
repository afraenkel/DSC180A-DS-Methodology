#!/usr/bin/env python

import sys


def main(n1, n2):

    print(
        list(range(n1, n2))
    )

    return


if __name__ == '__main__':
    L = sys.argv[1:]
    n1, n2 = int(L[0]), int(L[-1])
    main(n1, n2)
