#!/usr/bin/env python

import ftools
import sys

def main():
    if len(sys.argv) < 3:
        print 'Usage: %s <filename> <mode>' % sys.argv[0]
        return

    fd = file(sys.argv[1], 'r')


    ftools.fadvise(fd.fileno(),mode=sys.argv[2])

    fd.close()


if __name__ == '__main__':
    main()
